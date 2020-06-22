import random                                                                  #require it for genrating random index for "random" mode


#function to take only integer input
def int_input(string):
    try:
        m=int(input(string))
        return m                                                                #returns only when the input is integer
    except:
        m=int_input(string)                                                     #recalling the function if the input is non-integer
        return m


#function that makes list of the issues
def issue_lst_maker():
    n=int_input("Enter the number of issues:")                                  #only integer input allowed
    lst_issue=list()                                                            #list of issues
    for i in range(n):
        print("Enter the issue number "+str(i+1)+":")
        issue=input()
        lst_issue.append(issue.rstrip())
    return lst_issue                                                            #returning the list of issues


#function that  makes the list of agents
def agent_lst_maker():
     agent_number=int_input("Enter the number of agents:")
     agent_lst=list()                                                           #list of agents
     for i in range(agent_number):
       dct=dict()                                                               #dictionary created for an individual agent containing their respective details
       print("Details of "+str(i+1)+" agent:-")
       name=input("Enter the name of agent:")                                   #name of agent
       is_available=input("Enter 'y' if available else 'n':")                   #availaiblity of agent

       #converting the is_available to bool and checking if the input is either of 'y' or 'n'
       if(is_available=='y' or is_available=='Y'):
           is_available=True
       if(is_available=='n' or is_available=='N'):
           is_available=False
       if(is_available==True):
           m=False
       elif(is_available==False):
           m=False
       else:
           m=True

       #It will ask to enter the value of is_available untill the user enters either of 'y' or 'n'
       while(m):
           is_available=input("Please input a proper input for is_available:")
           if(is_available=='y' or is_available=='Y'):
               is_available=True
           elif(is_available=='n' or is_available=='N'):
               is_available=False
           if(is_available==True):
               m=False
           elif(is_available==False):
               m=False
           else:
               m=True

       #asking time of availaiblity if avaialable,if not avaialable settinf default value to zero
       if(is_available):
           available_since=int_input("Please input time for which the agent has been available free(in mins):")
       else:
           available_since=0
       roles=input("Plese input the roles for which the agent look  out:")
       dct.update({"name":name,"is_available":is_available,"available_since":available_since,"roles":roles})  #updating the dictionary created for the indivaidual agent
       agent_lst.append(dct)                                                    #appending the dict to list of agents
     return agent_lst                                                           #returns the list of agents containing dictionary of details of agents


#function for selection of proper agents as well as to take input of mode
def agent_selector(issu,agent_lst):
    mode=input("Enter the mode of agent selection:")
    mode=mode.lower()
    mode=mode.rstrip()
    lst=list()
    for agent in agent_lst:
        if(agent["is_available"]):
            lst.append(agent)

    #checks the roles of issues match agents domain or not
    update_lst=list()
    for agent in lst:
        if(issu  in agent["roles"]):                                            #checks if domain of  agent is relevent to the issue
            update_lst.append(agent)

    if(len(update_lst)==0):                                                     #checks whether any agents are avaialable or not
        return "No agents available."

    #carry out neccesary steps related to all available mode
    if(mode=="all available"):
        if(len(update_lst)==0):                                                 #checks whether any agents are avaialable or not
            return ("No agents available.")
        final_lst=update_lst
        return final_lst                                                        #returns list which contains classes of agents titled as their name and who are available and have respective domain

    #carry out neccesary steps related to least busy mode
    if(mode=="least busy"):
        max_time=0
        lst1=list()                                                             #creates list to store the time of availaiblity of agents
        for agent in update_lst:                                                #stores the time of availaiblity
            lst1.append(agent["available_since"])
        max_time=max(lst1)                                                      #finds out maximum time that a agent has remained available
        final_lst=list()
        for agent in update_lst:
            if(agent["available_since"]==max_time):
                final_lst.append(agent)                                         #list contain only one agent  that has remain maximum time avaialable i.e least busy
        if(len(final_lst)==0):                                                  #checks whether any agents are avaialable or not
            return("No agents available.")
        return final_lst

    #carry out neccesary steps related to random mode
    if(mode=="random"):
        n=len(update_lst)                                                       #number of agents filtered out of availaiblity and their domains
        random_num=random.randint(0,n-1)                                        #a random index number for the available filtered list
        if(n==0):                                                               #checks whether any agents are avaialable or not
            return "No agents available."
        final_lst=list()
        final_lst.append(update_lst[random_num])
        return final_lst                                                        #returns a random agent from the list
    return "Enter proper mode."



#Our main function that takes issues list as argument and takes input of agents and their details along with mode of Selections
def agent_selector_main(issue_lst):
    agent_lst=agent_lst_maker()                                                 #takes input of agent and their details
    sollution_lst=list()                                                        #final list that contain list of agents from given diffrent issues
    for issue in issue_lst:
        solln=agent_selector(issue,agent_lst)                                   #calling function for selecting proper agent as well as to take input of mode
        if(solln=="No agents available." or solln=="Enter proper mode."):       #appending strings to the sollution_lst
              sollution_lst.append(solln)
        else:
              selected_lst=list()                                               #list for names of agents selected for solving the issue
              for agent_dict in solln:
                  selected_lst.append(agent_dict["name"])                       #appending the names of agents
              sollution_lst.append(selected_lst)                                #appending the list of names to the list containinglists of selected agents for issue
    return sollution_lst


#main function for joining all the function logic together
def main():
    issue_lst=issue_lst_maker()                                                 #creating list of issues
    result=agent_selector_main(issue_lst)                                       #getting result as list of list of names for a given issue list
    for solln in result:                                                        #printing the list of names by iteratiing through the list of sollutions for each issues
        print(solln)
    return "All Agent Selections for given Issues done."                        #returning a end statemment (implemented to  counter the printing of none in testing ;))


if __name__ == '__main__':
    check=main()
    print(check)                                                                #printing the  end statemment
