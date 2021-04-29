# Test Driven Ranges

This exercise extends the [Battery Monitoring] use-case.

The charging current varies during the process of charging.
We need to capture the range of current measurements -
what range of currents are most often encountered while charging.

> **DO NOT** jump into implementation! Read the example and the starting task below.

## Example

### Input

Consider a set of periodic current samples from a charging session to be:
`3, 3, 5, 4, 10, 11, 12`

### Functionality

The continuous ranges in there are: `3,4,5` and `10,11,12`.

The task is to detect the ranges and
output the number of readings in each range.

In this example,

- the `3-5` range has `4` readings
- the `10-12` range has `3` readings.

### Output

The expected output would be:

```
Range, Readings
3-5, 4
10-12, 3
```

## Tasks

Start test-driven development:

1. Establish quality parameters for your project: What is the maximum complexity you would allow? How much duplication would you consider unacceptable? What is the coverage you'll aim for?
Adapt/adopt/extend the `yml` files from one of your workflow folders.

1. Write the smallest possible failing test.

1. Write the minimum amount of code that'll make it pass.

1. Write the next failing test.

Implement one failing test and at least one passing test:


| test case                                                  | Result        | Remarks
|------------------------------------------------------------|---------------|---
test_with_in_range_for_min_minus_one                         | passing       | 
test_with_in_range_for_max_plus_one                          | passing       | 
test_with_in_range_for_min_plus_one                          | passing       | 
test_with_in_range_for_max_minus_one                         | failing       |#Making test fail:Actual expected value=True
test_getpreviousitem_for_empty_list                          | passing       | 
test_getpreviousitem_for_one_element                         | passing       | 
test_getpreviousitem_for_elemet_not_in_list                  | passing       |
test_getpreviousitem_for_two_element                         | failing       |#Making test fail:Actual expected value=1
test_get_ranges_list_for_empty_list                          | passing       |
test_get_ranges_list_list_for_one_element                    | passing       |
test_get_ranges_list_for_two_element                         | failing       |#Making test fail:Actual expected value=[[1,2]]
test_get_ranges_list_for_multitple_element                   | passing       |
test_range_list_to_range_dict_list_for_empty_list            | passing       |
test_range_list_to_range_dict_list_for_list_with_one_range   | failing       |#Making test fail:Actual expected value=[{'lowerLimit': 1, 'upperLimit': 2, 'Count': 0}]
test_range_list_to_range_dict_list_for_list_with_two_range   | passing       |
test_ranges_with_most_often_occurences_log_for_none          | passing       |
test_ranges_with_most_often_occurences_log_for_empty_list    | passing       |
test_ranges_with_most_often_occurences_log_for_one_reading   | passing       |
test_ranges_with_most_often_occurences_log_for_two_reading   | passing       |
test_charging_current_log_for_multiple_reading               | passing       |
