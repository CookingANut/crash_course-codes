def describe_pet(pet_name,animal_type='dog'):
#def describe_pet(animal_type='dog',pet_name):  即使指定了默认值，python依然将这个实参视为位置实参，如果函数调用中只包含宠物的名字，这个实参将关联到函数定义的第一个参数，这就是需要将pet_name放在形参开头的原因
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')   #即便使用关键字参数也没用，是因为本身函数def describe_pet(animal_type='dog',pet_name):这样定义就是有问题，因为这样定义使得位置实参调用会有问题，所以定义就是有问题的
#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参，这让Python依然能够准确地解读位置实参