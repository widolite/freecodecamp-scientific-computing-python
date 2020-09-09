import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, cant in balls.items():
            for x in range(cant):
                self.contents.append(color)

    def __str__(self):
        return str(self.contents)

    def draw(self, quantity):
        draw_list = []
        if len(self.contents) < quantity:
          draw_list = self.contents
          self.contents = []
        else:
          for x in range(quantity):
            contents_len = len(self.contents)
            draw_list.append(self.contents.pop(random.randrange(contents_len)))
        return draw_list


def convert_balls_into_dict(balls):
    temp_expected_balls = {}
    for ball in balls:
        try:
            temp_expected_balls[ball] += 1
        except KeyError:
            temp_expected_balls[ball] = 1
    return temp_expected_balls


def experiment(hat, expected_balls={}, num_balls_drawn=0, num_experiments=0):

    match = 0
    exp_expected_balls = []
    for color, cant in expected_balls.items():
      for x in range(cant):
        exp_expected_balls.append(color)

    for experiment in range(num_experiments):
      
      copy_hat = copy.deepcopy(hat)
      
      balls_drawn = copy_hat.draw(num_balls_drawn)
      
      control = True
      
      for ball in exp_expected_balls:
        if ball in balls_drawn:
          balls_drawn.remove(ball)
        else:
          control = False
      if control:
        match += 1
                
    probability = match / num_experiments
    return probability
