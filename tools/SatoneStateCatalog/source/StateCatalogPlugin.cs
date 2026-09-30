using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using UnityEngine;

namespace SatoneStateCatalog
{
    [BepInPlugin("scaleph.satone.statecatalog", "Satone State Catalog", "0.1.0")]
    public sealed class StateCatalogPlugin : BaseUnityPlugin
    {
        [Serializable]
        public sealed class Catalog
        {
            public int schemaVersion = 1;
            public string updatedUtc = "";
            public List<Entry> entries = new List<Entry>();
        }

        [Serializable]
        public sealed class Entry
        {
            public string category = "";
            public string code = "";
            public string modelCode = "";
            public string description = "";
            public string observedUtc = "";
            public string updatedUtc = "";
        }

        private sealed class CurrentItem
        {
            public string category;
            public string code;
            public string modelCode;
            public string Label { get { return category + " | " + (modelCode == "" ? "" : modelCode + " / ") + code; } }
            public string Key { get { return category + ":" + code; } }
        }

        private static readonly BindingFlags Members = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance;
        private readonly List<CurrentItem> _current = new List<CurrentItem>();
        private readonly Dictionary<string, string> _drafts = new Dictionary<string, string>();
        private Catalog _catalog = new Catalog();
        private Rect _window = new Rect(40, 40, 760, 600);
        private Vector2 _scroll;
        private string _selected = "";
        private string _description = "";
        private string _status = "Press Refresh after opening the room.";
        private string _loadError = "";
        private string _directory;
        private object _room;
        private bool _open;
        private float _nextRefresh;

        private void Awake()
        {
            _directory = Path.Combine(Paths.ConfigPath, "SatoneStateCatalog");
            LoadCatalog();
        }

        private void Update()
        {
            if (Input.GetKeyDown(KeyCode.F10))
            {
                _open = !_open;
                if (_open) Refresh();
            }
            if (_open && Time.realtimeSinceStartup >= _nextRefresh)
            {
                _nextRefresh = Time.realtimeSinceStartup + 0.75f;
                Refresh();
            }
        }

        private void OnGUI()
        {
            if (_open) _window = GUI.Window(14732981, _window, DrawWindow, "Satone State Catalog (F10 to close)");
        }

        private void DrawWindow(int windowId)
        {
            GUILayout.Label("Current in-game IDs. Select a visible item, describe it, then Save.");
            if (GUILayout.Button("Refresh current state", GUILayout.Height(25))) Refresh();
            _scroll = GUILayout.BeginScrollView(_scroll, GUILayout.Height(245));
            foreach (CurrentItem item in _current)
            {
                if (GUILayout.Button((item.Key == _selected ? "> " : "   ") + item.Label, GUILayout.Height(24))) Select(item);
            }
            GUILayout.EndScrollView();

            GUILayout.Label("Selected: " + (FindSelected() == null ? "(none; open the room first)" : FindSelected().Label));
            GUILayout.Label("Your visual description (you may type Chinese):");
            _description = GUILayout.TextArea(_description, GUILayout.Height(105));
            if (FindSelected() != null && GUILayout.Button("Save this item and update the document", GUILayout.Height(30))) SaveSelected();
            GUILayout.Label("Recorded entries: " + _catalog.entries.Count + " | " + _status);
            GUILayout.Label("Output: " + _directory);
            GUI.DragWindow(new Rect(0, 0, _window.width, 24));
        }

        private void Refresh()
        {
            try
            {
                if (_room == null || IsDestroyedUnityObject(_room)) _room = FindRoom();
                if (_room == null)
                {
                    _current.Clear();
                    _status = "RoomGameManager unavailable; load the room, then Refresh.";
                    return;
                }
                var items = new List<CurrentItem>();
                object views = Get(_room, "_windowViewService");
                if (views != null) ReadViews(views, items);
                object costume = Get(_room, "_costumeChangeService");
                if (costume != null) ReadCostume(costume, items);
                object decoration = Get(_room, "_decorationService");
                if (decoration != null) ReadDecorations(decoration, items);
                _current.Clear();
                _current.AddRange(items);
                if (FindSelected() == null)
                {
                    if (_selected != "") _drafts[_selected] = _description;
                    if (_current.Count > 0) Select(_current[0]);
                    else { _selected = ""; _description = ""; }
                }
                _status = _current.Count + " current IDs detected.";
            }
            catch (Exception e)
            {
                _status = "Read failed: " + e.GetType().Name;
                Logger.LogWarning("State snapshot failed: " + e);
                _room = null;
            }
        }

        private static bool IsDestroyedUnityObject(object value)
        {
            var unityObject = value as UnityEngine.Object;
            return !ReferenceEquals(unityObject, null) && !unityObject;
        }

        private static object FindRoom()
        {
            foreach (MonoBehaviour candidate in Resources.FindObjectsOfTypeAll<MonoBehaviour>())
            {
                if (candidate && candidate.GetType().FullName == "Bulbul.RoomGameManager" && candidate.gameObject.activeInHierarchy)
                    return candidate;
            }
            return null;
        }

        private static void ReadViews(object views, List<CurrentItem> items)
        {
            MethodInfo isActive = views.GetType().GetMethod("IsActiveWindow", Members);
            if (isActive == null) return;
            Type enumType = isActive.GetParameters()[0].ParameterType;
            foreach (object code in Enum.GetValues(enumType))
            {
                try
                {
                    if (true.Equals(isActive.Invoke(views, new[] { code })))
                        items.Add(new CurrentItem { category = "window", code = code.ToString(), modelCode = "" });
                }
                catch { /* One optional view can be unavailable in an older game build. */ }
            }
        }

        private static void ReadCostume(object costume, List<CurrentItem> items)
        {
            object model = Get(costume, "_currentModelType");
            object skin = Get(costume, "_currentSkinType");
            if (model != null && skin != null)
                items.Add(new CurrentItem { category = "costume", code = skin.ToString(), modelCode = model.ToString() });
        }

        private void ReadDecorations(object decoration, List<CurrentItem> items)
        {
            object data = Call(decoration, "get_DecorationSaveData");
            IDictionary dictionary = Get(data, "DecorationDic") as IDictionary;
            if (dictionary == null) return;
            object masterLoader = Get(_room, "_masterDataLoader");
            object master = Get(masterLoader, "DecorationMaster");
            foreach (DictionaryEntry pair in dictionary)
            {
                try
                {
                    object active = Get(pair.Value, "IsActive");
                    if (!true.Equals(Get(active, "Value"))) continue;
                    string category = "decoration";
                    string modelCode = "";
                    if (master != null)
                    {
                        object categoryData = Call(master, "GetCategoryBySkin", pair.Key);
                        object modelData = Call(master, "GetModelBySkin", pair.Key);
                        object type = Get(categoryData, "CategoryType");
                        object modelType = Get(modelData, "ModelType");
                        if (type != null) category = "decoration/" + type;
                        if (modelType != null) modelCode = modelType.ToString();
                    }
                    items.Add(new CurrentItem { category = category, code = pair.Key.ToString(), modelCode = modelCode });
                }
                catch (Exception e) { Logger.LogWarning("Skipped one decoration ID: " + e.GetType().Name); }
            }
        }

        private static object Get(object value, string name)
        {
            if (value == null) return null;
            Type type = value.GetType();
            FieldInfo field = type.GetField(name, Members);
            if (field != null) return field.GetValue(value);
            PropertyInfo property = type.GetProperty(name, Members);
            return property == null ? null : property.GetValue(value, null);
        }

        private static object Call(object value, string name, params object[] args)
        {
            if (value == null) return null;
            MethodInfo method = value.GetType().GetMethod(name, Members);
            return method == null ? null : method.Invoke(value, args);
        }

        private CurrentItem FindSelected()
        {
            return _current.Find(i => i.Key == _selected);
        }

        private void Select(CurrentItem item)
        {
            if (_selected != "") _drafts[_selected] = _description;
            _selected = item.Key;
            string draft;
            Entry saved = _catalog.entries.Find(e => e.category == item.category && e.code == item.code);
            _description = _drafts.TryGetValue(_selected, out draft) ? draft : saved == null ? "" : saved.description;
        }

        private void LoadCatalog()
        {
            string path = Path.Combine(_directory, "catalog.json");
            if (!File.Exists(path)) return;
            try
            {
                _catalog = JsonUtility.FromJson<Catalog>(File.ReadAllText(path, Encoding.UTF8));
                if (_catalog == null || _catalog.schemaVersion != 1 || _catalog.entries == null)
                    throw new InvalidDataException("Unexpected catalog schema");
            }
            catch (Exception e)
            {
                _catalog = new Catalog();
                _loadError = e.Message;
                _status = "Could not read catalog.json; save disabled to protect the file.";
                Logger.LogError("Catalog load failed: " + e);
            }
        }

        private void SaveSelected()
        {
            CurrentItem item = FindSelected();
            if (item == null) return;
            if (_loadError != "") { _status = "Save disabled: " + _loadError; return; }
            if (string.IsNullOrWhiteSpace(_description)) { _status = "Enter a description first."; return; }
            string now = DateTime.UtcNow.ToString("o");
            Entry entry = _catalog.entries.Find(e => e.category == item.category && e.code == item.code);
            bool newEntry = entry == null;
            if (newEntry) entry = new Entry { category = item.category, code = item.code, observedUtc = now };
            entry.modelCode = item.modelCode;
            entry.description = _description.Trim();
            entry.updatedUtc = now;
            if (newEntry) _catalog.entries.Add(entry);
            _catalog.updatedUtc = now;
            try
            {
                Directory.CreateDirectory(_directory);
                WriteAtomic(Path.Combine(_directory, "catalog.json"), JsonUtility.ToJson(_catalog, true));
                _drafts[_selected] = entry.description;
                WriteAtomic(Path.Combine(_directory, "appearance_catalog.md"), MakeMarkdown(_catalog));
                _status = "Saved JSON and Markdown at " + DateTime.Now.ToString("HH:mm:ss") + ".";
            }
            catch (Exception e)
            {
                _status = "Write failed: " + e.Message;
                Logger.LogError("Catalog write failed: " + e);
            }
        }

        private static void WriteAtomic(string path, string content)
        {
            string temporary = path + ".tmp";
            File.WriteAllText(temporary, content, new UTF8Encoding(false));
            if (!File.Exists(path)) { File.Move(temporary, path); return; }
            try { File.Replace(temporary, path, path + ".bak"); }
            catch (PlatformNotSupportedException)
            {
                File.Copy(path, path + ".bak", true);
                File.Copy(temporary, path, true);
                File.Delete(temporary);
            }
        }

        private static string MakeMarkdown(Catalog catalog)
        {
            var result = new StringBuilder("# Satone appearance catalog\n\n");
            result.Append("Updated (UTC): ").Append(catalog.updatedUtc).Append("\n\n");
            result.Append("| Category | Current internal ID | Model ID | Description | Updated (UTC) |\n");
            result.Append("|---|---|---|---|---|\n");
            foreach (Entry entry in catalog.entries)
                result.Append("| ").Append(Cell(entry.category)).Append(" | ").Append(Cell(entry.code))
                    .Append(" | ").Append(Cell(entry.modelCode)).Append(" | ")
                    .Append(Cell(entry.description)).Append(" | ").Append(Cell(entry.updatedUtc)).Append(" |\n");
            return result.ToString();
        }

        private static string Cell(string value)
        {
            return (value ?? "").Replace("\\", "\\\\").Replace("|", "\\|")
                .Replace("\r\n", "<br>").Replace("\n", "<br>").Replace("\r", "<br>");
        }
    }
}
