# This is a reproduction of MAPPO paper

https://arxiv.org/pdf/2103.01955

Ensure that you have x86_64 machine otherwise you won't be able to run Starcraft II.

Steps to reproduce results:
1. Run ./install_starcraft2.sh`
2. Change wandb entity in eeml.ipynb from "godjan-yuki-the-seal" to your own one. Also you would need to have an account at https://wandb.ai/, it's free
3. Execute cells of eeml.ipynb in consecutive order to launch training.
   - if you'd like to run only SMAC environment(longer), then you can ignore cells marked with "# Only related to MPE Simple spread"
   - if you'd like to run only MPE Simple spread(faster), then you can ignore cells marked with "# Only related to SMAC"