import unittest
import battery_monitoring

class battery_monitoringTest(unittest.TestCase):

  #Test for 'with_in_range' function  
  def test_with_in_range_for_min_minus_one(self):#(min-1)<(min)
    self.assertFalse(battery_monitoring.with_in_range(19, 20, 30))

  def test_with_in_range_for_max_plus_one(self):#(max)<(max+1)
    self.assertFalse(battery_monitoring.with_in_range(31, 20, 30))
    
  def test_with_in_range_for_min_plus_one(self):#(min+1)>(min)
    self.assertTrue(battery_monitoring.with_in_range(21, 20, 30))
    
  def test_with_in_range_for_max_minus_one(self):#(max-1)<(max)
    self.assertFalse(battery_monitoring.with_in_range(29, 20, 30))#Making test fail:Actual expected value=True

  #Test for 'getpreviousitem' function
  def test_getpreviousitem_for_empty_list(self):
    self.assertTrue(battery_monitoring.getpreviousitem([],0)==None)
    
  def test_getpreviousitem_for_one_element(self):
    self.assertTrue(battery_monitoring.getpreviousitem([0],0)==None)
    
  def test_getpreviousitem_for_elemet_not_in_list(self):
    self.assertTrue(battery_monitoring.getpreviousitem([1,2],3)==None)
    
  def test_getpreviousitem_for_two_element(self):
    self.assertTrue(battery_monitoring.getpreviousitem([1,2],2)==0)#Making test fail:Actual expected value=1

  #Test for 'get_ranges_list' function
  def test_get_ranges_list_for_empty_list(self):
    self.assertTrue(battery_monitoring.get_ranges_list([])==[])

  def test_get_ranges_list_list_for_one_element(self):
    self.assertTrue(battery_monitoring.get_ranges_list([1])==[])

  def test_get_ranges_list_for_two_element(self):
    self.assertTrue(battery_monitoring.get_ranges_list([1,2])==[])#Making test fail:Actual expected value=[[1,2]]

  def test_get_ranges_list_for_multitple_element(self):
    self.assertTrue(battery_monitoring.get_ranges_list([1,2,4,6,7,8])==[[1,2],[6,8]])

  #Test for 'range_list_to_range_dict_list' function
  def test_range_list_to_range_dict_list_for_empty_list(self):
    self.assertTrue(battery_monitoring.range_list_to_range_dict_list([])==[])

  def test_range_list_to_range_dict_list_for_list_with_one_range(self):
    self.assertTrue(battery_monitoring.range_list_to_range_dict_list([[1,2]])==[])#Making test fail:Actual expected value=[{'lowerLimit': 1, 'upperLimit': 2, 'Count': 0}]

  def test_range_list_to_range_dict_list_for_list_with_two_range(self):
    self.assertTrue(battery_monitoring.range_list_to_range_dict_list([[1,2],[4,6]])==[{'lowerLimit': 1, 'upperLimit': 2, 'Count': 0},{'lowerLimit': 4, 'upperLimit': 6, 'Count': 0}])


  #Test for 'ranges_with_most_often_occurences' function
  def test_ranges_with_most_often_occurences_log_for_none(self):
    self.assertTrue(battery_monitoring.ranges_with_most_often_occurences(None)==None)

  def test_ranges_with_most_often_occurences_log_for_empty_list(self):
    self.assertTrue(battery_monitoring.ranges_with_most_often_occurences([])==[])

  def test_ranges_with_most_often_occurences_log_for_one_reading(self):
    self.assertTrue(battery_monitoring.ranges_with_most_often_occurences([1])==[])

  def test_ranges_with_most_often_occurences_log_for_two_reading(self):
    self.assertTrue(battery_monitoring.ranges_with_most_often_occurences([1,2])==[{'lowerLimit': 1, 'upperLimit': 2, 'Count': 2}])
    
  #Test for 'charging_current_log' function
  def test_charging_current_log_for_multiple_reading(self):
    self.assertTrue(battery_monitoring.charging_current_log([3, 3, 5, 4, 10, 11, 12])==None)

if __name__ == '__main__':
  unittest.main()

