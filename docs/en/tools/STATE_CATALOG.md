[简体中文](../../zh-CN/tools/STATE_CATALOG.md) | [English](STATE_CATALOG.md) | [日本語](../../ja/tools/STATE_CATALOG.md)

# SatoneStateCatalog: F10 appearance catalog

[Home](../README.md) · [Build instructions](BUILD_STATE_CATALOG.md) · [IDs awaiting observation](OBSERVED_IDS.md)

This independent BepInEx plugin needs neither AIChat nor SPP. F10 reads the active window view, outfit, glasses and decoration IDs, letting you describe what you actually see. The catalog supports future appearance awareness/conversational control; those features are not implemented by this tool.

## Install and record

Install BepInEx 5, then copy the [prebuilt SatoneStateCatalog.dll](../../../tools/SatoneStateCatalog/prebuilt/SatoneStateCatalog.dll) to the game's `BepInEx/plugins`. Launch and press F10. The tool UI is English; descriptions can use Chinese, English or Japanese. Select the current item, write its appearance and choose **Save this item and update the document**.

It writes `BepInEx/config/SatoneStateCatalog/catalog.json` and `appearance_catalog.md`, preserving a `.bak` of the previous file. Saving the same category/style ID updates that entry rather than adding duplicates. Multiple active window effects should all be listed and described as a combination.

A description such as “thin black round frames” for `Glasses_2 / Glasses_2B` is only an example, not a verified mapping. Internal names do not establish color or appearance. Observe the actual item.

## Scope and safety of saves

The prebuilt DLL was compiled against local BepInEx/Unity references; [BUILD_INFO](../../../tools/SatoneStateCatalog/prebuilt/BUILD_INFO.json) records its provenance. It was not fully tested in the game. It reads active state and does not unlock items, alter achievements or write the game save. If incompatible, remove the DLL.

Locked items that cannot be activated cannot be visually described through this read-only tool. Use your own backup/separate test save when appropriate; do not replace your only save with an unknown “100%” save. There is no automatic unlock or preview mode.

## Files and contributions

`catalog.json` has `schemaVersion`, `updatedUtc` and `entries`. Each entry includes `category`, `code`, `modelCode`, `description`, `observedUtc`, `updatedUtc`. You can share the catalog JSON/Markdown in an Issue after checking its contents. This guide does not submit anything automatically.
