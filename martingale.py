"""Assess a betting strategy.  		   	  			    		  		  		    	 		 		   		 		  

Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			    		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			    		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			    		  		  		    	 		 		   		 		  

Template code for CS 4646/7646  		   	  			    		  		  		    	 		 		   		 		  

Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			    		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			    		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			    		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			    		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			    		  		  		    	 		 		   		 		  
or edited.  		   	  			    		  		  		    	 		 		   		 		  

We do grant permission to share solutions privately with non-students such  		   	  			    		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			    		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			    		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			    		  		  		    	 		 		   		 		  

-----do not edit anything above this line---  		   	  			    		  		  		    	 		 		   		 		  

Student Name: Rahul Jayakrishnan  		   	  			    		  		  		    	 		 		   		 		  
GT User ID: rjayakrishnan3  		   	  			    		  		  		    	 		 		   		 		  
GT ID: 903281837 		   	  			    		  		  		    	 		 		   		 		  
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def author():  		   	  			    		  		  		    	 		 		   		 		  
    return 'rjayakrishnan3' # replace tb34 with your Georgia Tech username.

def gtid():  		   	  			    		  		  		    	 		 		   		 		  
    return 903281837 # replace with your GT ID number

def get_spin_result(win_prob):  		   	  			    		  		  		    	 		 		   		 		  
    result = False
    if np.random.random() <= win_prob:
        result = True
    return result

def test_code():
    win_prob = 0.47368 # set appropriately to the probability of a win
    np.random.seed(gtid()) # do this only once
    print get_spin_result(win_prob) # test the roulette spin

def simple_sim():
    win_prob = 0.47368
    winnings = np.zeros(1000)
    bet_amount = 1
    won = False
    max_itr = 1000
    i = -1
    while i < max_itr-2:
        i = i + 1
        if winnings[i] < 80:
            won = get_spin_result(win_prob)
            if won:
                winnings[i+1] = winnings[i] + bet_amount
                bet_amount = 1


            else:
                winnings[i + 1] = winnings[i] - bet_amount
                bet_amount = bet_amount * 2

        else:
            winnings[i+1:] = 80
            break

    return winnings

def exp_1():
    max_try = 10
    max_itr = 1000
    alltrials = np.empty((max_try,max_itr))
    for i in range(max_try):
        alltrials[i] = simple_sim()
        plt.plot(alltrials[i],label="Trial "+str(i+1))
    # print alltrials
    plt.axis([0, 300, -256, 100])
    plt.title("Figure 1")
    plt.xlabel("Spins")
    plt.ylabel("Episode Winnings")
    plt.legend(loc='lower right')
    plt.savefig("figure1.png")
    max_try = 1000
    alltrials = np.empty((max_try, max_itr))
    for i in range(max_try):
        alltrials[i] = simple_sim()
    mean_alltrials = np.mean(alltrials,axis=0)
    std_alltrials = np.std(alltrials, axis=0)
    meanplusstd = mean_alltrials + std_alltrials
    meanminusstd = mean_alltrials - std_alltrials
    plt.clf()
    plt.plot(mean_alltrials,label='mean')
    plt.plot(meanplusstd,label='Mean+stdev')
    plt.plot(meanminusstd,label='Mean-stdev')
    plt.axis([0, 300, -256, 100])
    plt.title("Figure 2")
    plt.xlabel("Spins")
    plt.ylabel("Mean Episode Winnings")
    plt.legend(loc='lower right')
    plt.savefig("figure2.png")
    median_alltrials = np.median(alltrials,axis=0)
    medianplusstd = median_alltrials + std_alltrials
    medianminusstd = median_alltrials - std_alltrials
    plt.clf()
    plt.plot(median_alltrials,label='Median')
    plt.plot(medianplusstd,label='Median+stdev')
    plt.plot(medianminusstd,label='Median-stdev')
    plt.axis([0, 300, -256, 100])
    plt.title("Figure 3")
    plt.xlabel("Spins")
    plt.legend(loc='lower right')
    plt.ylabel("Median Episode Winnings")
    plt.savefig("figure3.png")
    return



def realistic_sim():
    win_prob = 0.47368
    winnings = np.zeros(1000)
    bet_amount = 1
    won = False
    max_itr = 1000
    bankroll = 256
    i = -1
    while i < max_itr-2:
        i = i + 1
        if winnings[i] <-255:
            winnings[i + 1:] = -256
            break
        if winnings[i] < 80:
            won = get_spin_result(win_prob)
            if won:
                winnings[i + 1] = winnings[i] + bet_amount
                bankroll += bet_amount
                bet_amount = 1



            else:
                winnings[i + 1] = winnings[i] - bet_amount
                bankroll -= bet_amount
                bet_amount = min(bet_amount * 2,bankroll)


        else:
            winnings[i + 1:] = 80
            break
    return winnings

def exp_2():
    max_itr = 1000
    max_try = 1000
    alltrials = np.empty((max_try, max_itr))
    for i in range(max_try):
        alltrials[i] = realistic_sim()
    mean_alltrials = np.mean(alltrials, axis=0)
    std_alltrials = np.std(alltrials, axis=0)
    meanplusstd = mean_alltrials + std_alltrials
    meanminusstd = mean_alltrials - std_alltrials
    plt.clf()
    plt.plot(mean_alltrials,label='Mean')
    plt.plot(meanplusstd,label='Mean+stdev')
    plt.plot(meanminusstd,label='Mean-stdev')
    plt.axis([0, 300, -256, 100])
    plt.title("Figure 4")
    plt.xlabel("Spins")
    plt.ylabel("Mean Episode Winnings")
    plt.legend(loc='lower right')
    plt.savefig("figure4.png")
    median_alltrials = np.median(alltrials, axis=0)
    medianplusstd = median_alltrials + std_alltrials
    medianminusstd = median_alltrials - std_alltrials
    plt.clf()
    plt.plot(median_alltrials,label='Median')
    plt.plot(medianplusstd,label='Median+stdev')
    plt.plot(medianminusstd,label='Median-stdev')
    plt.axis([0, 300, -256, 100])
    plt.title("Figure 5")
    plt.xlabel("Spins")
    plt.ylabel("Median Episode Winnings")
    plt.legend(loc='lower right')
    plt.savefig("figure5.png")
    return
# add your code here to implement the experiments

if __name__ == "__main__":
    np.random.seed(gtid())
    exp_1()
    exp_2()
    print "Figures generated"






