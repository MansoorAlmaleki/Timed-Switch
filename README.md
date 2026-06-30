**Op amp timed switch**


**Components used:**
   *∙1x 100uF capacitor*
   *∙1x 1K resistor*
   *∙1x 200ohm resistor* 
   *∙1x 10K variable resistor*
   *∙1x Lm358(any op amp can be used)*

This is a timed switch which relies on the RC circuit where the voltage is fed into
the non-inverting input of an op amp.
The inverting input os hooked up to a variable voltage divider ro set the trigger threshold
voltage, where a lower thershold voltage will lead to a faster trigger


**Calculating time until trigger**

![Alt text](Equation2.jpeg)

*the equation is rearranged to*

![Alt text](Equation1.jpeg)

with my circuit a 100uF capacitor and a 1K resistoe gives an RC time constant od 100ms, our activation voltage is > 2.8
