from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2

class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        # getting the initial picture
        obs, _, _, _ = env.step([0,0])
        # convect in for work with cv
        img = cv2.cvtColor(np.ascontiguousarray(obs), cv2.COLOR_BGR2RGB)
        
        # add here some image processing
        height, width, _ = img.shape 

        lower_range = np.array([170,170,0])
        upper_range = np.array([255,255,150])

        condition = True
        while condition:
            obs, reward, done, info = env.step([1, 0])

            img = np.ascontiguousarray(obs)
            mask = cv2.inRange(img, lower_range, upper_range)
            area = cv2.countNonZero(mask)

            if (area >= 0.06*height*width):
                condition = False 
            else:
                condition = True                      
                env.render()
