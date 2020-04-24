import torch
#from /home/chase/pytorch-OpCounter/thop/profile.py import profile

from profileForBN import profile

import numpy as	np
import tensorflow as tf

from net import	model

def	get_flops(model, numExitPoints):
	
	input = torch.randn(1,	 3,	32,	32)
	macs, _ = profile(model,	inputs=(input, ), verbose=False)
	
	
	# from	 the THOP git:
	# "The	 FLOPs is approximated by multiplying by two."
	macs = sorted([2 * int(mac) for mac in macs[0:numExitPoints]], key=int)
	
	
	return macs
	
print('FLOPs in	BranchyNet:',get_flops(model(), 4))
