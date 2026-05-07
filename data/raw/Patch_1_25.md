### Contents

- 1Expansion Features
- 2Free Features
- 3Gamebalance3.1Economy3.2Governments3.3Religion3.4Units3.5War & Peace3.6Other
- 3.1Economy
- 3.2Governments
- 3.3Religion
- 3.4Units
- 3.5War & Peace
- 3.6Other
- 4AI4.1Diplomacy4.2Economy4.3War4.4Other
- 4.1Diplomacy
- 4.2Economy
- 4.3War
- 4.4Other
- 5Interface5.1Country5.2Icons/Art5.3Other
- 5.1Country
- 5.2Icons/Art
- 5.3Other
- 6Usermodding6.1Commands6.2Effects6.3Logging6.4Modifiers6.5Triggers6.6Other
- 6.1Commands
- 6.2Effects
- 6.3Logging
- 6.4Modifiers
- 6.5Triggers
- 6.6Other
- 7Script7.1Achievements7.2Decisions7.3Events7.4Ideas7.5Missions7.6Setup7.7Other
- 7.1Achievements
- 7.2Decisions
- 7.3Events
- 7.4Ideas
- 7.5Missions
- 7.6Setup
- 7.7Other
- 8Bugfixes
- 9References
Patch 1.25, aka "England", was released on 2018-03-20[1]with the checksum0fb2. The patch was released alongside theRule Britanniaexpansion.

### Expansion Features

- Nations now have an Innovativeness value, ranging from 0.0 to 100.0.
- Knowledge Sharing lets you speed up the adoption of Institutions in the target country.
- Naval Doctrine Wooden Wall now gives a combat roll bonus of 1 in neighboring coastal provinces.
- Added Coal Trade Good. Trading in Coal gives 10% extra Goods Produced nationally. Local bonus is 20% State Maintenance reduction.
- Added potential for Coal to a number of provinces worldwide.
- Added Furnace Manufactory that boosts national goods produced by 5% instead of local produced goods.
- The Steer Trade diplomatic action and peace treaty can be used to make merchants in the recipient country steer trade value towards your trade nodes.
- Added 15 Anglican events, including DHE to convert to Anglicanism as a British-culture nation.
- Added 14 Irish missions
- Added 15 Scottish missions
- Added English Missions
- Added British Missions
- [Purple Phoenix] Updated the Purple Phoenix DLC for the new Mission System.
### Free Features

- Added map changes to The British Isles, France and Low Countries
- Added New National Ideas to British Isles and Low Countries
- Lobby/Start Screen: Added news banner (shown first time game is started after an update with new news content).
- Reworked how gold is demanded in peace offers: 5 war score now equal one loan size of target, and maximum WS on gold is 25.
- Missions System has been completely reworked, displaying all available missions for a nation in a dedicated tab
- Diversified SFX for Papacy-style interfaces.
- 10 Achievements added
### Gamebalance

#### Economy

- Reduced most permanent sources of land maintenance cost reduction.
- Increased tech effect on land maintenance from 0.01 to 0.02
- Reduced amount of production and trade efficiency gained from tech
#### Governments

- Tenures Abolition Policy no longer useless for Celestial Empires
#### Religion

- you no longer break alliance or support liberty relations when changing the religion.
#### Units

- It is no longer possible to Conform to template Condottieri (or pending Condottieri).
#### War & Peace

- At most 25 war score can be demanded as gold in peace.
- War Score cost for Transfer Trade Power reduced to 30%
- Tributary overlord is not called into independence wars between a tributary and his subject. Sukhothai rejoice!
- Support independence is no longer canceled after one month if the overlord of the subject is a tributary.
#### Other

- To set Player attitude to Friendly towards a country now requires said country to have 50 opinion of player.
### AI

#### Diplomacy

- AI slightly more weights in neighbors that might declare on them in prewar power calculations.
- AI will now consider giving provinces to subject in peace even if they have vital interest on them.
- Made getting Friendly attitude from AI directly depend on opinion to a degree; this is an attempt to fix the bug that for unknown reasons made it very rare.
- AI overlord cancelling Tributary relation or being cancelled by overlord will have -1000 towards acceptance for the duration of the opinion modifier.
- Added explicit check to forbid AI from canceling Transfer trade power or Trade steering when an agreement to their benefit is in force, and they are not preparing war.
- Fixed ruler personality induced war declaration disclosures and added this to Babbling Buffoon and Malevolent personalities as well.
- Fixed AI acceptance modding for custom diplomatic actions.
#### Economy

- AI will now use Statute in Restraint of Appeals decision under limited circumstances. AI with this decision active will never reject Anglicanism.
- AI is now aware of more types of diplomatic expenses when performing budget calculations, hence less likely to underestimate budget.
- Free Thinker and Scholar personality rulers are more likely to Knowledge share.
- An AI country maxed out on tech will no longer try to advance to higher tech (this was reducing late game performance and preventing it from e.g. developing provinces instead).
- AI is now more keen to repair unmothballed ships during peace if they have no loans.
- AI is now able to decrease tariffs (again?)
- Fixed AI increase in budget when rich, so it will spend more on army and navy if being very rich.
- AI is now much more likely to build force limit buildings.
- AI now deprioritizes building force limit/manpower/sailor buildings until they have built some economic buildings.
- AI can now destroy buildings to build better ones if out of building slots when they are rich.
#### War

- Mostly undid "AI prefers to siege with 1 or 2 regs above minimum of limit" change unless fort level is one. It caused other issues currently too complex for AI to deal with.
- Capped number of days in a row an AI army will skip processing for during peace to 15 to avoid unresponsiveness when preparing war.
- Fixed AI massing on borders before declaring war (for immersion), if there isn't too high threat nearby.
- Trimmed down number of independent AI armies for countries with many regiments as this was being a performance drain.
- Tweaked non-tributary subjects declaring wars (colonial nations) to require a greater advantage, as to create fewer "overlord must rescue them" situations.
- Fixed issue where AI wouldn't merge many small transport fleets due to waiting for an admiral assignment it wouldn't decide to make anyway.
- AI made more likely to choose fort provinces as fleet bases to avoid easy capture.
- Added guard against AI launching doom stacking invasions into one province islands that already have enough troops (this works for any friendly units already arrived).
- AI will no longer use armies to explore when there are threats nearby said army.
- AI can now split their transport fleet when they feel safe about doing so and army to be transported is smaller than fleet.
- Fixed case where army would refuse to board transport because target location is held by enemy controller (really old code not making sense).
- Fixed exploration nations' AI splitting up most or all of their armies into 5k stacks due to reassigning conquistador.
- AI should be slightly more proactive against transports landing troops on their home shores.
- Fixed AI warship building; it can now build 5-10 times as large war fleets under favorable circumstances.
- AI now keeps a home fleet consisting of warships that's not allowed to stray far from their home coast.
- Revised number of admirals the AI recruits.
- AI no longer unassigns admiral from fleet as soon as it leaves port to another fleet in port.
- AI considers maneuver more important than before when estimating navy power and admiral skill.
- Reduced willingness of AI to suicide navies that would enter battle early with a way too powerful enemy fleet because of expecting reinforcements.
- Probably fixed exiled armies with splinters stuck unable to reach their base due to gathering up.
- Fixed cause of fleets stuck waiting for 0 unit armies.
- AI will try to keep a minimum fraction of its armies at home rather than sending them abroad to fight. This is however constrained by its splitting logic.
- Invading AI army stuck and unable to path to departure port will now disband. This is less bad than tying up a large part of the AI's force (including freed splinters).
- Tried to make AI less adamant about transporting troops to own areas with little actual military threat, as well as diverting troops from areas with significant actual threat.
- AI slightly more likely to assign leaders to main armies rather than splinters, and especially than divisions.
- AI can now simultaneously invade with multiple armies in same area provided there are enough enemies there (rather than exclusively with one army at a time).
- Fixed major bug in region assignment system that made most assignments fantasy comparatively speaking.
- Fixed invasion splinter consolidation behavior.
- Tightened up AIs use of repairing fleets for transport (especially, it will no longer assign such a fleet and then let army sit frozen and wait for it to repair).
#### Other

- Revisited exploration logic to make it work as intended w.r.t. not using entire fleet for it. AI will also stop exploring during war properly.
- AI regions are now different from geographic regions and are calculated to optimize AI, will hopefully help with idiot Mamluk AI.
- Fixed crash caused by AI trying to raise janissaries in lost states.
### Interface

#### Country

- Fixed country names sometimes appearing in very strange places when using Random New World
- Land/Navy force limit values/modifiers (considering local autonomy) are shown on map and macro builder selecting Regimental Camp and Shipyard.
#### Icons/Art

- Added new flag for Cornwall
- Armies drilling around now have a very notable yellow "Drilling" in their tooltip.
- When a human player is at war with another human player, a blue flame will now be shown in the outliner instead of the standard red.
#### Other

- Clicking on an achievement's progress/requirements in the achievement browser will now highlight relevant provinces on the map that you need to fulfill the Achievement.
- Clicking a decision requirement will now highlight relevant provinces on the map.
### Usermodding

#### Commands

- Added "innovativeness" console cmd.
- Added "norevolts" console command.
- Added "repair" [ships] console command.
- Updated "economy" console command to also display AI budget.
- Added "powerspend_count" console command.
- Added "assert" console command to check trigger argument (if trigger evaluates false, test failure is invoked).
#### Effects

- Added "change_innovativeness" effect (Country scope. Range [-100.0, 100.0], capped to [0.0, 100.0]).
- Added complete_mission effect
#### Logging

- Removed error logging of dynamic ( ex. [USER=1182520]@root[/USER] ) flags.
- Fixed error log flooding of "undefined event target" when using global_event_target.
#### Modifiers

- Added innovativeness static modifier.
- Added the modifier type institution_growth. When applied to a province, it will grow all institution by this value, with special case handling for knowledge_sharing.
- Added the province modifier knowledge_sharing added to any province where knowledge sharing is growing an institution.
#### Triggers

- Added "innovativeness" trigger (Country scope. Range: [0.0, 100.0]).
- "else" and "else_if" now also works for the trigger version of "if"
- Added is_capital_of trigger
- has_province_modifier trigger now supports triggered province modifiers (takes triggered province modifier trigger key, checks both active and non-active triggered modifiers).
- Added has_active_triggered_province_modifier trigger (takes triggered province modifier trigger key).
- Added support for provinces_to_highlight for missions, decisions and achievements
- Make continent trigger support provinces (Instead of only continent tags and country tags)
- Added num_of_foreign_hre_provinces trigger.
- Added has_mission trigger to check if scope tag has mission available
- Add number of consorts trigger.
- Add captured ships with Boarding naval doctrine trigger.
- Add island provinces trigger.
#### Other

- Added the define NDefines::NDiplomacy::PEACE_COST_GOLD_STEP to specify maximum number of loans worth of gold that can be taken from giver.
- Changed the semantics of define PEACE_COST_GOLD_STEP to set WS per loan.
- Added PEACE_COST_STEER_TRADE define to specify peace cost of the Steer trade peace option.
- Added the define DIPLOMATIC_ACTION_KNOWLEDGE_SHARING_ACCEPTANCE_MULT to control AI's tendency to use Knowledge Sharing based on acceptance.
- Changed church aspect objects effect to be named modifier instead.
- Added the defines KNOWLEDGE_SHARING_DURATION_YEARS and KNOWLEDGE_SHARING_COST_PERCENT_MONTHLY to control Knowledge Sharing.
- Added define EXTRA_SURPLUS_WHEN_NEEDING_BUILDINGS for AI to make them save more money as long as they need to construct buildings.
- Added INVADING_MIN_HOME_RATIO to specify minimum of armies AI should keep at home.
- Added HOME_FLEET_MAX_RATIO to specify the upper limit number of warships AI should keep as a home fleet.
### Script

#### Achievements

- Added 10 new achievements
#### Decisions

- Added province highlighting for decisions.
- Added decision to adopt Sikh Religion for Muslims.
#### Events

- Added 15 Innovativeness events
- Added option in Margaret of Anjou event to make her a consort. Event can no longer trigger if there is already a consort.
- Cruelty of Mercenaries now requires at least 15 units of Mercenaries, rather than 1.
- Added 22 events relating to the Industrial Revolution.
- Added 1 price change event for Coal.
- The event for Toyotomi Hideyoshi now lets you choose him as your heir.
#### Ideas

- Burgundian Ambition is now 15% Goods Produced.
#### Missions

- Added province highlighting for missions.
- Added French missions
- Added Mamluk missions
- Added Persian Missions. The Persian flavor events "Reforms of Ismail" and "The Shrine of Najaf" are now triggered through missions instead of mean time to happen.
- Updated Missions for Gujarat for the new Mission System
- Updated Missions for Orissa for the new Mission System
- Updated Missions for Oman for the new Mission System
- Updated Missions for High American Tech Group for the new Mission System
- Updated Missions for Korea for the new Mission System
- Updated Missions for Hisn Kayfa for the new Mission System
- Updated Missions for Lubeck for the new Mission System
- Updated Missions for Netherlands for the new Mission System
- Updated Missions for Spain and Castile for the new Mission System
- Updated Missions for England for the new Mission System
- Updated Missions for Portugal for the new Mission System.
- Updated Missions for Austria for the new Mission System.
- Updated Missions for Tirol and Styria for the new Mission System.
- Updated Missions for the Ottoman Empire for the new Mission System.
- Fleshed out Byzantine Mission to conquer Venice reward a bit.
- Updated and Reworked Missions for Timurids, Afghanistan, Transoxiana, and Ajam for the new Mission system
- Updated Base Game Missions for the Byzantines for the new Mission System.
- Added Missions for Bohemia
- Added Missions for Burgundy, focusing on Lotharingia and Arelat
- Added short Mission Chain for Rassids and Aden
#### Setup

- Added The Isles as a vassal of Scotland in 1444
- Dijon is now an Inland Center of Trade.
- János Hunyadi no longer treated as a regency.
- Revamped areas a bit in Northern France and the Low Countries.
- Split Bourgogne into Dijonnais and Auxerrois.
- Removed Limburg Province and replaced it with Upper Guelders. Much of old Limburg now belongs to the province of Liege.
- Added 4 provinces to Ireland.
- Added 15 provinces to the Island of Great Britain.
- Added 3 provinces to the Lowlands Region.
- Added 8 provinces to the French Region.
- Added Tyrconnell country tag Ireland.
- Added Faly country tag in Ireland.
- Added Ormond country tag in Ireland.
- Added Munster (MacCarthy Mor) country tag in Ireland.
- Added Mann revolter tag.
#### Other

- Added startup screens for Irish minors, Provence, Brittany, and Scotland.
- You can now pick the Siberian Clan Council government in the Nation Designer.
### Bugfixes

- You can no longer reinforce your armies for free by drilling them.
- Added even more consistent coloring in tutorial overview.
- Fixed bug in trade policy event 9 that would make it impossible to get new maps from it.
- Fixed bad check in tribal federation event 6.
- Breaking Vassalization is no longer limited to Art of War (clearly not WAD).
- Fixed wrong primary culture for Hojo, Hosokawa and Tokugawa.
- Fixed sound not playing when becoming Defender of the Faith for certain religions.
- Fixed CTD when trying to move a trade end node in nudger.
- Fixed minor heir name display bug.
- Removed different religious school penalty when playing without CoC as it was inconsistent with DLC feature.
- Fixed bug where subject wasn't able to call its overlord into war when said overlord had warned other party, despite UI claiming otherwise.
- Modding: Fixed trade routes no longer being written when using the nudge tool (broke in 1.23).
- Modding: Fixed trade routes not showing when first opening the nudge tool.
- Modding: Added info dialog when trying to select a Trade Node with no outgoing routes.
- MP: Fixed banned players getting a message about being kicked instead of banned.
- Fixed swapped option texts for Japanes flavor event 50, "A Son Finds His Way Home".
- Startup screen for Austria no longer makes claims about the ability of Albert the Magnanimous twice.
- Fixed an event that could swap the religion of a province that had a Center of Reformation.
- Fixed a bug where the Japanese Flavor Event "Silver Pavilion" could trigger in a province that already had a Cathedral.
- Fixed freeze when having the same unit multiple times in province unit list.
- Fixed CTD in ai_acceptance in custom diplomatic actions.
- Fixed La Malinche's distinct lack of culture.
- Forming Japan now properly sets a flag so it cannot be recycled by the same country.
- Local Institution spread no longer shown in national modifier view.
- Grand Embassy event series should now be less confused about gender.
- Fixed Timeline FoW exploit.
- When the emperor enacts "Revoke Privilegia" it does not matter if it's capital is outside of HRE for liberty desire calculation purpose
- The Surrender of Maine event no longer refers to the wrong monarch taking matters into his own hands.
- When a Center of Reformation is created, it will now automatically stop conversion by other Centers of Reformation.
- Fixed CTD and added error log if trying to use add/remove_province_triggered_modifier with invalid modifier.
- Fix the Declare War dialog: the overlord of colonial nations will not defend the colonial nation in case of war against other colonial nations or natives.
- Fixed CTD when using the "run" console command with scripted triggers.
- Fix new (empty) provinces when loading old saves
- Added flag to prevent war of the roses from potentially happening twice
- Primitives no longer get Naval Reformers in their advisor pool
- Fixed wrong scope for institution_events.26 MTTH.
- Units can no longer be Conformed to Template while movement is locked.
- Yet another fix for AI sending subsidies < 0.1 ducats
- Make trading cities start with ideas group if appropriate
- Make Constantinople the Capital decision now changes religion in Constantinople to ROOT religion rather than Sunni
- Fixed so that you cannot refill garrisons unless they are controlled by you or a current war ally.
- Hostile coring cost province modifier no longer disappears for annexed countries as long as they are the most "hostile coring costing" claim in the province.
- Troop counts over 1 million in war overview now show with 2 decimals.
- Troop counts in war overview are no longer hidden to observer.
- Fixed the ability to create empty "ghost armies" when transporting across water via automatic transport missions.
- Fixed crash when trying to build a manufactory locally in a province.
- Fixed scoping bug for continent trigger in some trade policy events.
- Fixed error when using the "cede_province = ---" command.
### References

1. ↑Forum,1.25 England Update released [checksum 0fb2] - not for problem reports, 2018-03-20