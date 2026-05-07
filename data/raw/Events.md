This article istimelessand should be accurate for any version of the game.

Eventsoccur throughout the course of play ofEU4. There are a whole range of events in the game, which can result in positive, negative and mixed outcomes for a player's country. They take the form of a pop-up notification on the player's screen, which may present a player with a choice, or may simply inform the player of the consequences and require they acknowledge the event has occurred. After four months on the same date, the first choices gets autoselected, if the player did not choose an option.

### Contents

- 1Triggered-only events
- 2Pulse events2.1Date calculations for x-year pulses2.2Date calculations for the monthly pulse
- 2.1Date calculations for x-year pulses
- 2.2Date calculations for the monthly pulse
- 3Mean time to happen
- 4See also
### Triggered-only events[edit|edit source]

Triggered-only events are events that occur as a result of a nation's actions. The events can happen to that same nation or to another nation altogether. The needed trigger can be as simple as one nation choosing a particular option in an event or complex as taking over a certain province, thereby enabling an event at another nation. The events are usually fired immediately or within a short amount of time from being triggered.

### Pulse events[edit|edit source]

Pulse events[1]are random events that happen within regular intervals of time. One of their main purposes is to provide interactions and a sense of randomness within the game. That being said, while the events areboundto happen they are still based on player's actions; for example, for anexploration eventto fire, the player needs to have an explorer/conquistador in the process of exploration.

The events are grouped together into different sets depending on their purpose (regular gameplay or mechanic related) and assigned weights within their respective sets. Each set is programmed to fire in regular time intervals. The time intervals range from yearly intervals and up-to 5 year intervals. It is important to note however that there are several same-year intervals and it does not mean they'll fire at the same date. When the interval arrives an event is picked at random from within the set and fired. Events with higher weights have higher chances to fire than the lower ones[2]. Having certain modifiers, idea groups, provinces etc. can increase or decrease some events' weights. Most pulses also have a weight for getting no event at all.

##### Date calculations for x-year pulses[edit|edit source]

Yearly pulses happen each year. The 2 year pulses always happen in years which are divisible by 2 and the 3 year pulses happen in years divisible by 3. The years in which the 4 and 5 year pulses happen depend on the tag order id[3]of the country which gets the event. They happen if(year−tag order id){\displaystyle ({\text{year}}-{\text{tag order id}})}is divisible by 4 (5 for 5 year pulses). The day of the year on which the pulse happens for a country is calculated with the following formula(this applies to all x-year pulses):

Failed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): {\displaystyle (\text{year} + \text{tag order id} + \text{pulse offset}) \bmod 365}

Day 0 is January 1st and day 364 is December 31st.

A spreadsheet to compute the exact date of each pulse for any given tag can be foundhere. It can't be edited directly, so it either has to be downloaded and opened in Excel(or another compatible program) or it can be copied in google sheets. To use the spreadsheet go to the first tab titled "Pulse Dates" and in the top left corner of that sheet simply edit the cells withyellowtext (note all user inputs are inyellowtext while calculations are in black text) . There are two inputs required for the spreadsheet to work namely (1) selecting the game version you are using (2) entering the target country's tag into the tag field. Not required, but for ease of reference, you can enter a target year to view and the sheet will only display dates in that year or later. The sheet will automatically determine the tag order and calculate the pulse date. Note that on that pulse date an event (for that particular pulse's associated group of events) may or may not fire depending on the probabilities associated with any event in that group. Moreover, the events in a pulse group are mutually exclusive, meaning only one event may fire at a time, assuming an event fires at all.

The pulse offset is different for each pulse:

##### Date calculations for the monthly pulse[edit|edit source]

There is also a monthly pulse in the game, but it is only used by mods. The day of the months for the pulse is calculated with the following formula:

Failed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): {\displaystyle \left((\text{tag order id}) \bmod (\text{days in month})\right) + 1}

For example Ragusa with the tag order id36will have the monthly pulse on the 6th in months which have 31 days(becauseFailed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): {\displaystyle (36 \bmod 31) + 1 = 6}), on the 7th in months which have 30 days and on the 9th of February which has 28 days.

### Mean time to happen[edit|edit source]

Other events are not triggered but have a chance of happening at any time if their conditions are met. These events are controlled by a mean time to happen (MTTH).

This mechanic determines the time it takes for an event to trigger, measured in months. Yet since events are probabilistic, there is a small chance an event may happen very quickly, or possibly never at all during the game. For example, if an event had a MTTH of 120 months, it means that usually it would take around a decade for the event to trigger. Certain factors may increase or decrease MTTH for an event, such as country's leader's quality, national stability, and so on.

Assuming the probabilities are calculated in the same manner asin EU3, then despite the name MTTH is actually themediantime, or half-life, for the event to trigger, i.e., the amount of time during which there is a 50% chance of the event occurring by that time, rather than themean(average).

The engine checks whether an event occurs everyEVENT_PROCESS_OFFSETdays, set to 20 at default. The chance per check is

Failed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): 1 - 2^{-t_c / t_{1/2} }

whereFailed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): t_cis theEVENT_PROCESS_OFFSETandFailed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): t_{1/2}is the median.

This approximates the "ideal" probability

Failed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): 1 - 2^{-t / t_{1/2}}

whereFailed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): tis the amount of time that passes. The approximation is best for a long MTTH.

The medianFailed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): t_{1/2}and meanFailed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): \overline{t}are related by

Failed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): \overline{t} = \frac{t_{1/2}}{\ln 2} \approx 1.44 t_{1/2}

In terms of the mean, the ideal probability is:

Failed to parse (SVG (MathML can be enabled via browser plugin): Invalid response ("Math extension cannot connect to Restbase.") from server "https://en.wikipedia.org/api/rest_v1/":): 1 - e^{-t / \overline{t}}

For a repeating event the number of occurrences within a given number of checks is given by abinomial distribution, which may be approximated by aPoisson distributionfor a long MTTH.

### See also[edit|edit source]

- List of events files
1. ↑For a list of Pulse events seeList of event lists.
1. ↑The weight for no event and all weights of events who's triggers are fulfilled are added together to arrive at the total weight. The chance for each event is its weight divided by the total weight.
1. ↑The tag order id of a country can be found in the first column of thetag order list.