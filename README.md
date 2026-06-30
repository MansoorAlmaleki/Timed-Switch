**Op amp timed switch**


**Components used:**
   *∙1x 100uF capacitor*
   *∙1x 1K resistor*
   *∙1x 200ohm resistor* 
   *∙1x 10K variable resistor*
   *∙1x Lm358(any op amp can be used)*

![Alt text](CircuitSchematic.png)

![Alt text](BreadboardCircuit.png)


This is a timed switch which relies on the RC circuit where the voltage is fed into
the non-inverting input of an op amp.
The inverting input os hooked up to a variable voltage divider ro set the trigger threshold
voltage, where a lower thershold voltage will lead to a faster trigger


**Calculating time until trigger**

![Alt text](Equation2.jpeg)

*the equation is rearranged to*

![Alt text](Equation1.jpeg)

**Circuit measurment**
![Alt text](SignalOverTime.jpg)
*Blue plot is the RC circuit voltage over time*
*yellow plot is the Op amp Vout voltage over time

with the given circuit a 100uF capacitor and a 1K resistor gives an RC time constant of 100ms, with the activation voltage of 2.85V (Vtarget) the resulting time to trigger the switch takes 51.8ms
