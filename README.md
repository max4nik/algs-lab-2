# Task

Горила Джекі із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків
(piles) з бананами, у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під
охороною, але охорона здійснює обхід зоопарку на Н годин, протягом якого Джекі може
поласувати своєю улюбленою стравою.
Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть
К бананів звідти. Якщо кошик має менше, ніж К бананів, вона з'їдає всі банани з нього і
більше не буде їсти бананів протягом цієї години.
Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш
ніж охоронці повернуться.
Визначіть мінімальне ціле число К таким чином, щоб Джекі могла з'їсти всі банани на
складі протягом Н годин, поки повернеться охорона.

## Solution

- defining low and high borders for binary searching:
    - low border is sum of all elements in `piles` divided by `hours` for better performance
- doing binary search:
    - if passes condition `can_eat_in_time()` - (`real_hours` needed for eating all piles with `probable_speed` are less then `hours_to_eat`) : set current maximal value to mid value
    - else if do not pass condition `can_eat_in_time()`: set current minimal value to mid value
    - return current minimal value as solution whenever `maximal_value` will be less or equal to `minimal_value`
    
## How-to-use instructions
- clone repository
- open project folder in console
- do either:
    - run `python solution/bananas.py` in console
    <br/>
    or
    <br/>
    - open `solution` folder
    - run `python bananas.py`

## Algorithm analysis

### Time complexity
O(N(log(MAX_FROM_PILES - SUM_OF_PILES/hours) + 1))
    <br/>
    <br/>
    where:
- N is length of `piles` list
- MAX_FROM_PILES is biggest element in `piles`
- SUM_OF_PILES is sum of all elements in `piles`
 
### Space complexity
O(1)
