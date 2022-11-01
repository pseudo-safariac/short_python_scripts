height: float | int = int(input('Enter your height in cm:\n'))
weight: float | int = int(input('Enter weight in kg:\n'))

def bmi_calculation(height : float, weight : float)-> str | None:
	"""_Summary_
	The function receives a user's height and weight, then computes the BMI according to the formula suggested by the CDC.
	
	__Source1__ : https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used.
	__Source2__ : https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm

	Args:
		height (float): Height in centimetres.
		weight (float): Weight in kilograms.

	Returns:
		Returns a string with information about the BMI index of the user using the input received.
	"""
	bmi: float | int = (weight/height/height)*10000

	if bmi <= 18.5:
		return str('You are underweight')
	elif bmi >= 18.5 and bmi <= 24.9:
		return str('You are of normal weight')
	elif bmi >= 25 and bmi <= 29.9:
		return str('You are overweight')
	elif bmi >= 30:
		return str('You are Obese.')

print(bmi_calculation(height, weight))