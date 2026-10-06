[简体中文](../../zh-CN/systems/CHAT_UI.md) | [English](CHAT_UI.md) | [日本語](../../ja/systems/CHAT_UI.md)

# Chat interface and history

[Documentation](../README.md#systems) · AIChat 1.18.28 + SPP 5.10.8

Press **F9** to open AIChat. Settings and chat remain separate areas, and chat has distinct history, input, send and voice controls. The interface now supports Chinese, English and Japanese; use the language option appropriate to you. Older guides/screenshots may still show Chinese labels.

## Input and history

Enter sends; Shift+Enter inserts a newline. See [voice input](VOICE_INPUT.md) for F8 and microphone controls. Story playback, disconnection or an unfinished turn can still restrict input.

The default history view shows the **latest 50 utterances**, not 50 complete question/answer pairs and not the storage limit. A custom retained configuration may specify another count. Original lines and AI exchanges keep their sources; displayed history, full local records and the context sent to a model are not identical lists.

Window history is `BepInEx/config/AIChatSatoneUX.history`, distinct from SPP's complete conversations and memories. Removing it does not erase all profiles or provider-side data.

## Background controls

The UI/behavior settings have separate background controls: window background and chat-history background. Both use **0.00 for fully transparent and 1.00 for fully opaque**, despite the transparency wording. Making a background transparent does not hide all text, borders and buttons. The history background does not also fill the input/settings areas.

Expand the custom chat-background color controls to adjust R/G/B (0–255) and lightness (0–100%). Lightness 0% is black and 100% white; changing it updates RGB while retaining hue/saturation where possible. This is not another opacity control or a filter over the whole game.

Dragging previews a change. Save and apply to persist it; cancel restores saved settings, and the default chat color can be restored separately. If old values remain after upgrading, inspect the retained configuration instead of deleting the entire save. See [data locations](../DATA_AND_PRIVACY.md).
