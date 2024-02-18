import scipy.io

sol_ch4 = scipy.io.loadmat('./solution_values4.mat')
sol_ch4_psnr = sol_ch4['psnr_solution_ch4']
sol_ch4_bpp = sol_ch4['bpp_solution_ch4']

sol_ch5 = scipy.io.loadmat('./solution_values5.mat')
sol_ch5_psnr = sol_ch5['psnr_solution']
sol_ch5_bpp = sol_ch5['bpp_solution']

my_ch4_PSNR = scipy.io.loadmat('./Final_PSNR_still_image_codec.mat')['Final_PSNR']
my_ch4_bpp = scipy.io.loadmat('./Final_rate_still_image_codec.mat')['Final_rate']

my_ch5_PSNR = scipy.io.loadmat('./Final_PSNR_video_codec.mat')['Final_PSNR']
my_ch5_bpp = scipy.io.loadmat('./Final_rate_video_codec.mat')['Final_rate']

import json

lambda_list = [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125, 0.00675]
ssf2020_psnr = []
ssf2020_bpp = []
mbt2018_mean_psnr = []
mbt2018_mean_bpp = []
elic2022_psnr = []
elic2022_bpp = []

for lambda_v in lambda_list:
    with open(f"./ssf2020/foreman0020-lambda_{lambda_v}_best-ans.json", "r") as f:
        json_data = json.load(f)
        ssf2020_psnr.append(json_data["results"]["psnr-rgb"])
        ssf2020_bpp.append(json_data["results"]["bpp"])
        
    with open(f"./mbt2018mean/lambda_{str(lambda_v).replace('.','_')}_best.json", "r") as f:
        json_data = json.load(f)
        mbt2018_mean_psnr.append(json_data["results"]["psnr-rgb"][0])
        mbt2018_mean_bpp.append(json_data["results"]["bpp"][0])
    
    with open(f"./elic2022/lambda_{str(lambda_v).replace('.','_')}_best.json", "r") as f:
        json_data = json.load(f)
        elic2022_psnr.append(json_data["results"]["psnr-rgb"][0])
        elic2022_bpp.append(json_data["results"]["bpp"][0])

import matplotlib.pyplot as plt
my_legend = ['sol_ch4', 'sol_ch5', 'my_ch4', 'my_ch5', 'VAE-inter (ssf2020)', 'VAE-intra (mbt2018-mean)', 'VAE-channelwised-intra (elic2022)']
fig, ax = plt.subplots()

plt.plot(sol_ch4_bpp[:,0], sol_ch4_psnr[:,0])
plt.plot(sol_ch5_bpp[:,0], sol_ch5_psnr[:,0])

plt.plot(my_ch4_bpp[0,:], my_ch4_PSNR[0,:])
plt.plot(my_ch5_bpp[0,:], my_ch5_PSNR[0,:])

plt.plot(ssf2020_bpp, ssf2020_psnr)
plt.plot(mbt2018_mean_bpp, mbt2018_mean_psnr)
plt.plot(elic2022_bpp, elic2022_psnr)

plt.legend(my_legend, bbox_to_anchor=(1.05, 1.0), borderaxespad=0, loc=2)

plt.savefig("./IVC_final_project_result.png", bbox_inches='tight')
plt.clf()