
#披萨配料选择程序

#******************************配料单以及配料价格定义部分***************************************
toppings_list = [           
    "牛肉",
    "洋葱",
    "榴莲",
    "西红柿",
    "火腿",
    "土豆",
]

price_list = {
    toppings_list[0]:"10",
    toppings_list[1]:"5",
    toppings_list[2]:"9",
    toppings_list[3]:"3",
    toppings_list[4]:"6",
    toppings_list[5]:"3",
}

price_dic = "\n\t配料单\n"
for topping, price in price_list.items():
    price_dic += topping + " ---------- " + price +"元\n"
print(price_dic)

#************************************信息提示以及参照初始设定部分*******************************

message1 = "\n请输入你需要在披萨中加入的配料："
message1 += "\n1.按回车输入下一个配料"
message1 += "\n2.输入“结束”就可以结束配料选择程序"
message1 +="\n"

message2 = "\n请继续输入你需要在披萨中加入的配料："
message2 +="\n"

message3 = "\n请输入你需要在披萨中加入的配料："
message3 +="\n"

active = True #程序激活
times_add = 1  #添加配料次数
times_false = 1   #输入错误次数
toppings_add = [] #用户自己的配料表
total_price = 0   #总价格

#*******************************主程序************************************

while active:
    #if times_add == 1:                                    #这里这些打#号的部分出现了比较难找的bug，bug就在 elif times_add > 1 and times_false > 1: 这里，原因在于，continue是直接跳到while开头，而不会执行最后的times_add +=1
    
    
    if times_add == 1 and times_false ==1:                 #导致if-elif-elif 没有一个满足的，直接跳过这三个判断语句，直接进入if toppings != "结束":。。。。。
        toppings = input(message1)
    
    #elif times_add > 1
    elif times_add > 1:#and times_false ==1:
        toppings = input(message2)
    
    elif times_add == 1 and times_false > 1:             # 如果使用者乱输入，则会使用message3提示，因为message1的重复提示次数太多没必要
    #elif times_add > 1 and times_false > 1:
        toppings = input(message3)
    
    
    
    if toppings != "结束":
        
    #*****************如果用户输入的不是是配料中的部分*****************
        if toppings not in toppings_list:            
            if times_false !=3:
                print(toppings + "不在菜单中，请不要输入配料单中没有的东西,连续输入三次无关的东西之后，程序自动关闭，" + "第" + str(times_false) + "次" )
                times_false += 1
                continue                           #乱输入前两次都从头跳到while重新循环
            elif times_false == 3:
                print("连续输入三次无关的东西之后，程序自动关闭。") 
                break                                    #第三次乱输入，直接结束程序
        
        
        
    #****************如果用户输入的是配料中的部分**********************
        print("\n我们会在披萨中添加" + toppings + ".")  
        times_false = 1  #重置输入失败次数       
        toppings_add.append(toppings)
        
        message4 = toppings_add[0]      #message4 目的是提示用户每次点完配料后，知道已经点了什么      
       
        for item3 in toppings_add[1:]:   #为了使最后点的配料之后没有“，”
            message4 += "," + item3      #将每次选的配料都加到message4
        
        #print(toppings_add)
        if len(toppings_add) > 1:
            print("已点配料： " + message4)         #配料大于1时打印这个
        else:
            print("已点配料： " + toppings_add[0])  #配料只有1时打印这个
    # times_add +=1  #这个必须在最后的原因是因为if 和 else 中间 如果用跳出判断的部分，默认为if语句已经结束，else就没有if就会出现fail     
    
    
    
    
    #*************当用户输入“结束”后，进入价格统计部分******************
    else:
        #active == False (这里是编写前的bug，需要注意)
        active = False        #切断循环
        #print(toppings_add)、
        for single_price in toppings_add:
            total_price += int(price_list[single_price])           #将用户配料表里的配料通过字典全部相加
        #print("\n配料价格总计：" + str(total_price) + "元")
        #print("————选择配料完成，程序结束")
        print("\n配料价格总计：" + str(total_price) + "元")
        print("————选择配料完成，程序结束\n")
    
    times_add +=1