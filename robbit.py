import math,time
#0 a1 b1 c1 d1
#45 a1 b0 c1 d0
#90 a1 b-1 c1 d-1
#135 a0 b-1 c0 d-1
#180 a-1 b-1 c-1 d-1
#225 a-1 b0 c-1 d0
#270 a-1 b1 c-1 d1
#315 a0 b1 c0 d1
M_A =0
M_B=1
M_C=2
M_D=3
class robbit:
    motors = [0,0,0,0]
    direction = 0
    speed = 0
    turn = 0

    def __init__(self,ramp_up=100,deadzone=10):
        self.deadzone = deadzone
        self.ramp_up = ramp_up
        for i in range(4):
            print "GERT set motor",i,"rampup to",ramp_up
            self.gertbotInterface()
            
    def stop(self):
        self.turn = 0
        self.speed = 0
        self.direction = 0
        self.adjustMotors()
        
    def gertbotInterface(self):
        for i in range(4):
            self.motors[i] = int(self.motors[i])
            if self.motors[i] == 0:
                print "GERT set motor",i,"to stop"
            elif self.motors[i] > 0:
                print "GERT set motor",i,"to forward"
                print "GERT set",i,"PWM to",self.motors[i]
            else:
                print"GERT set motor",i,"to backward"
                print "GERT set",i,"PWM to",abs(self.motors[i])

    def adjustMotors(self):
        X = math.sin(self.direction)*self.speed
        Y = math.cos(self.direction)*self.speed
        self.motors[M_A] = X
        self.motors[M_C] = X
        self.motors[M_B] = Y
        self.motors[M_D] = Y
        print self.motors
        self.motors[M_A] += self.turn
        self.motors[M_B] -= self.turn
        self.motors[M_C] -= self.turn
        self.motors[M_D] += self.turn
        print self.motors

        scaledown_up = max(self.motors[M_A],self.motors[M_B],self.motors[M_C],self.motors[M_D])/100.0
        scaledown_down = min(self.motors[M_A],self.motors[M_B],self.motors[M_C],self.motors[M_D])/100.0
        scaledown = max(abs(scaledown_up),abs(scaledown_down))
        if scaledown > 1:
            for i in range(4):
                self.motors[i] /= scaledown
                print scaledown,self.motors
                
        self.gertbotInterface()

    def setSpeed(self,speed):
        self.speed = max(self.deadzone,min(100,speed))
        if self.speed == self.deadzone:
            self.speed = 0

    def setDirection(self,direction):
        self.direction = math.radians(direction % 360)

    def setTurn(self,turn):
        self.turn = max(-100,min(100,turn))
        if self.turn > -self.deadzone and self.turn < self.deadzone:
            self.turn = 0
