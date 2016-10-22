from numpy import cos, pi, sqrt, sin

class FrictionPendulum:
	"""
	This class contains the relevant parameters for defining a pendulum as described in [1].
	The parameters to be fed as arguments to the constructor are:
		(1) u_k: The coefficient of friction.
		(2) R: The radius of the steel rod used to implement the friction.
		(3) h: The distance between the center of mass and the point of anchoring of the board.
		(4) L: The length of the wooden board used in the experiment.
		(5) init_angle: The initial angle to which the pendulum is drawn. It has to be entered in degrees.
	"""
	
	def __init__(self, u_k, R, h, L, init_angle):
		"""
		Initializes the pendulum object. 
		Arguments required are provided in documentation of the FrictionPendulum class.
		Please provide all argument values in meters or degrees.
		"""
		self.u_k = u_k
		self.R = R
		self.h = h
		self.L = L
		self.init_angle = init_angle * pi / 180
		
		g = 9.81
		w = g*h / (h**2 + L**2/12)
		self.w = sqrt(w)
	
	def theta(self, t = 0):
		"""
		Returns the current value of angle as a function of time.
		Argument is the time in SECONDS.
		Output value is in DEGREES.
		"""
		damp = 2 * self.u_k * self.R * self.w * t / (pi * self.h)
		if damp >= self.init_angle: return 0
		O = (self.init_angle - damp) * cos(self.w*t)
		O = O * 180 / pi	
		return O
	
	def omega(self, t):
		"""
		Returns the current time-derivative / rate of change of the angle theta as a function of time.
		Argument is the time in SECONDS. A Numpy Array of the same may also be provided.
		Output value is in DEGREES per second.
		"""
		damp = 2 * self.u_k * self.R * self.w * t / (pi * self.h)
		damp_coeff = 2 * self.u_k * self.R * self.w / (pi * self.h)
		if damp >= self.init_angle: return 0
		O = -self.w * (self.init_angle - damp) * sin(self.w * t) - damp_coeff * cos(self.w * t)
		return O
	
	def theta_gen(self, t=0):
		"""
		Generator function for the angle theta, with respect to time.
		"""
		damp = 0
		while self.init_angle >= damp:
			damp = 2 * self.u_k * self.R * self.w * t / (pi * self.h)
			if damp >= self.init_angle: yield t, 0
			O = (self.init_angle - damp) * cos(self.w*t)
			O = O * 180 / pi
			t += 0.01	
			yield t, O
	
	def omega_gen(self, t=0):
		"""
		Generator function for the angular velocity omega, with respect to time.
		"""
		damp = 0
		while self.init_angle >= damp:
			damp = 2 * self.u_k * self.R * self.w * t / (pi * self.h)
			damp_coeff = 2 * self.u_k * self.R * self.w / (pi * self.h)
			if damp >= self.init_angle: yield t, 0
			W = -self.w * (self.init_angle - damp) * sin(self.w * t) - damp_coeff * cos(self.w * t)	
			yield t, W
	
