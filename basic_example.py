import gym
import mani_skill.env

from gym import envs
for env in envs.registry.all():
    if str(env.id).find("OpenCabinetDoor-v0") >= 0:

        print(env.id)

print(1)
env = gym.make('OpenCabinetDoor-v0')
# nv = gym.make('OpenCabinetDoor_1077_link_0-v0')
print(2)
# full environment list can be found in available_environments.txt

# env.set_env_mode(obs_mode='state', reward_type='sparse')
env.set_env_mode(obs_mode='pointcloud', reward_type='dense')
print(3)
# obs_mode can be 'state', 'pointcloud' or 'rgbd'
# reward_type can be 'sparse' or 'dense'
print(env.observation_space) # this shows the structure of the observation, openai gym's format
print(env.action_space) # this shows the action space, openai gym's format

# for level_idx in range(0, 5): # level_idx is a random seed
for level_idx in range(0, 2): # level_idx is a random seed
    obs = env.reset(level=level_idx)
    print('#### Level {:d}'.format(level_idx))
    # for i_step in range(100000):
    for i_step in range(5):
        # env.render('human') # a display is required to use this function, rendering will slower the running speed
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action) # take a random action
        print('{:d}: reward {:.4f}, done {}'.format(i_step, reward, done))
        if done:
            break
env.close()
