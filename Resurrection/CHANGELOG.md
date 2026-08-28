# Version 81.3.0
Okay I experimented with content mods and ended up redoing a bunch of stuff. Wesley's and CodeRebirth are removed, in their place are a bunch more standard 
## Added
- Added the following mods which add new moons:
    - Generic Moons (by GenericGMD) adds 18 moons
    - Distinct Moon Variety adds 4 moons
- Added the following mods which add new items:
    - Cirno Fumo Scrap
    - Generic Scraps
    - Lethal Trading Cards
    - Monster Plushies
    - Scavenger Plushie
- Added the following mods which add new enemies:
    - Light Eater
- Added the following mods which add new suits:
    - More Vanilla Suits 
    - Fashion Company
- Added the following mods which add new cosmetics to the MoreCompany menu:
    - FashionableCompany
    - SimpleCompany
- Added the following quality of life mods:
    - BetterSprayPaint
    - ShowCapacity
- Added the following performance and bugfix mods:
    - ApparatusFix
- Added the following library mods:
    - ModelReplacementAPI
    - LethalStatus
    - LegaFusionCore
    - ManuLib
## Changed
- Updated some mods to the latest patch.
- LoadingScreen (before the game fully starts) now displays a custom modpack graphic.
## Removed
- Removed the Wesley's Moons set of mods (they aren't fully updated for v80).
    - This includes its dependencies, except for StarlancerAIFix (which is needed by EnemyEscape which is still in the pack).
- Removed several other mods:
    - CodeRebirth (playtesters found its additions overwhelming)
    - Moon_Day_Speed_Multiplier_Patcher (now part of LethalLevelLoader)


# Version 81.2.0
## Added
- Added a total of 16 new mods!
- Added the following **SPECIAL GUEST** mods (in the pack temporarily to see how we like them!):
    - Wesleys Moons (a high-quality mod adding 39 custom moons and a custom progression system)
    - Wesleys Interiors (twelve new interiors used by Wesleys Moons)
    - Wesleys Ememy Variants (variants of enemies used by Wesleys Moons)
    - Wesleys Weathers (four new weathers used by Wesleys Moons)
    - CodeRebirth (new mechanics, new enemies, new recruitable robots)
- Added the following gameplay mods:
    - StarlancerEnemyEscape (enemies have a chance to escape the facility)
- Added the following quality-of-life mods:
    - NoCompanyPenalties (Disables penalties for dying on the company moon because people keep trolling)
    - MainMenuVersion (Lets me customize the version number on the main menu)
- Added the following performance/bugfix mods:
    - ApparatusFix (Fixes some sound issues with the Apparatus)
- Added the following library mods:
    - DungeonGenerationPlus (a dependency of Wesley's Moons, expands compatibility for LC's dungeon generation)
    - StarlancerAIFix (a dependency of Wesley's Moons, automatically fixes enemy behavior inside/outside the facility based on spawn location)
    - LethalLevelLoader (a dependency of Wesley's Moons, provides a custom API to support adding custom moons/items/unlockables/enemies)
    - LCCutscene (a dependency of Wesley's Moons, a tool for creating immersive ingame cutscenes)
    - MaterialAssetRestorerCore (a dependency of Wesley's Moons, helps devs of custom moons use vanilla materials)
    - WaterAssetRestorer (a dependency of Wesley's Moons, helps devs of custom moons use vanilla water materials)
    - Moon_Day_Speed_Multiplier_Patcher (a dependency of Wesley's Moons, fixes several bugs tied to moons with a custom day speed multiplier)
    - CustomStoryLogs (a dependency of Wesley's Moons, lets you add custom story logs to your moons)
    - TerminalUtils (a bunch of dynamic preview and command related fixes for the terminal)
## Changed
- Fixed the config for ButteRyBalance to restore the vanilla Jetpack behavior (here you go Pread!)
- Disabled radio static playing in the Cruiser's radio.
- Bumped 32 mod versions, providing new bug fixes and stability improvements.
## Removed
- Removed several mods:
    - Imperium (should be out of the pack bother me if I accidentally readd it)
    - LCLocalFixes (it's marked as deprecated)


# Version 81.1.2
## Added
- Added the following gameplay mods:
    - Yippee Mod
## Changed
- Added random custom cave type visuals for the caves.
- Changed the loading screen tips to not be as long, and added more.
- Buffed the Teleporter to no longer drop tool items.
- Buffed the Inverse Teleporter to no longer drop tool items.
- Buffed the Radar Booster to be teleport-able (both Teleporter and Inverse Teleporter).
- Bumped a bunch of mod versions.
## Fixed
- Fixed an issue with Coroner where it would spam logs any time someone landed.
- Fixed an issue with Coroner where it wouldn't detect dying to a Bracken properly.
## Removed
- Removed several mods:
    - NiceChatEmptyMessageFix (it doesn't even work >:[ )

# Version 81.1.1
## Fixed
- Fixed an issue where the config was in the wrong spot and wasn't loaded.

# Version 81.1.0
Initial release.
## Added
- Added lots of dependency mods.
- Added lots of performance mods.
- Added lots of quality-of-life mods.
- Added several gameplay mods:
    - Abandoned Company Assets (custom scrap like abandoned flashlights)
    - Blue (blue weather)
    - ButteRyBalance (a bunch of scrap, enemy, and moon tweaks)
    - Fairer Fire Exits (tries to space fire exits more fairly)
    - General Improvements (improve the scanner to make it more reliable, custom monitors)
    - Lethal Casino (gamble scrap for value)
    - LethalFashion (adds a bunch of basic color suits)
    - MoreSuits (functionality to add more suits)
    - Mystery Button (an enemy found in the facility)
    - ScienceBird's Tweaks (zap gun buffs, unload shotgun)
    - Ship Windows (look outside the ship)
    - SmartEnemyPathfinding (masked can exit through fire exit now)
    - Wider Ship (more room for activities)