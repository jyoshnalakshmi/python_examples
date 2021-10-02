#function definition
def function_with_return_val():
  name = "jyoshna";
  return("(without args)my name is " +name);

name_value = function_with_return_val();
print(name_value);
#--------------------------------------------------
#Descrption: function with argument
#function definition:
#def function_with_return_val1(name):
#   statement
#   return
#
#function call:
#function_with_return_val(value1);
#
#-----------------------------------------------------------

def function_with_return_val1(name):
  name = "jyoshna";
  return("(with args)my name is " +name);

name_value1 = function_with_return_val1('jyo');
print(name_value1);

