#3_4
guest_list=["lulu","zhenfeng","yanyan","null"]
print("Dear "+guest_list[0]+", I sincerely invite you to my dinner.")
print("Dear "+guest_list[1]+", I sincerely invite you to my dinner.")
print("Dear "+guest_list[2]+", I sincerely invite you to my dinner.")
print("Dear "+guest_list[3]+", I sincerely invite you to my dinner.")

#3_5
print(guest_list[3].title()+" is busy now, I am afraid he could not come for dinner.")
del guest_list[3]
guest_list.append("null1")
print("Dear "+guest_list[3]+", I sincerely invite you to my dinner.")

#3_6
print("Cause I have found another bigger table for dinner, so I plan to invite more three people")
guest_list.insert(0,"null2")
guest_list.insert(3,"null3")
guest_list.append("null4")
print("Dear "+guest_list[0]+", I sincerely invite you to my dinner.")
print("Dear "+guest_list[3]+", I sincerely invite you to my dinner.")
print("Dear "+guest_list[6]+", I sincerely invite you to my dinner.")
#print(guest_list)

#3_7
print("Just knew the new table can't arrive in time, so I can only invite two of my guest.")
leave_guest1=guest_list.pop(0)
print("Sorry,"+leave_guest1+", I am afraid I can't invite you to dinner.")
leave_guest2=guest_list.pop()
print("Sorry,"+leave_guest2+", I am afraid I can't invite you to dinner.")
leave_guest3=guest_list.pop()
print("Sorry,"+leave_guest3+", I am afraid I can't invite you to dinner.")
leave_guest4=guest_list.pop(-2)
print("Sorry,"+leave_guest4+", I am afraid I can't invite you to dinner.")

print("Dear,"+guest_list[0]+", I still invite you to my dinner.")
print("Dear,"+guest_list[-1]+", I still invite you to my dinner.")

del guest_list[0]
del guest_list[0]
del guest_list[0]

print("Look,guest list is empty, like:"+str(guest_list)+".")


