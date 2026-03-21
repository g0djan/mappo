import multiprocessing as mp
mp.set_start_method('spawn', force=True)

def worker(conn, env_fn):
    try:
        env = env_fn()
    
        while True:
            cmd, data = conn.recv()
            if cmd == "step":
                reward, terminated, info = env.step(data)
                if terminated:
                    env.reset()
                obs = env.get_obs()
                state = env.get_state()
                avail_actions = env.get_avail_actions()
                conn.send((obs, state, avail_actions, reward, terminated, info))
            elif cmd == "reset":
                env.reset()
                obs = env.get_obs()
                state = env.get_state()
                avail_actions = env.get_avail_actions()
                conn.send((obs, state, avail_actions))
            elif cmd == "close":
                env.close()
                conn.close()
                break
    except Exception as e:
        import traceback
        traceback.print_exc()
        conn.send(("error", str(e)))
    finally:
        conn.close()

class SmacFactory:
    def __init__(self, map_name):
        self.map_name = map_name

    def __call__(self):
        from smac.env import StarCraft2Env
        return StarCraft2Env(map_name=self.map_name)