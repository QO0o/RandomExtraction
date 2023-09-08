import tkinter as tk
import random
import time

root = tk.Tk()
root.title('伪随机抽签器——2021级-13班-14号-猜猜我是谁')
root.config({'background': '#F5F5F5'})
root.geometry('800x500+250+85')
re_0 = tk.IntVar()# 创建一个变量，用于存储勾选框的状态
re_1 = tk.IntVar()
re_2 = tk.IntVar()
EXCLUDE_BOY = tk.IntVar()
EXCLUDE_GIRL = tk.IntVar()
ro_change_place=tk.IntVar()
class_size_print=tk.Label(root,text='本班  人',font=('宋体',15))
class_size=tk.Entry(root,textvariable=tk.StringVar(root,39),width=2,bd=0)
first_girl=tk.Entry(root,textvariable=tk.StringVar(root,25),width=2,bd=0)
first_girl_print=tk.Label(root,text='号起为女生',font=('宋体',12))
all_label=[str(i) for i in list(range(1,int(class_size.get())+1))]
random_num=str(random.choice(all_label))
label = tk.Label(root, text=f"{random_num}",font=('黑体',70),heigh=3,width=11,borderwidth=3,relief="solid")
label.place(x=389,y=149,anchor='center')
ro_place = tk.Checkbutton(root, text="随机位置", variable=ro_change_place,command=lambda:label.config(fg='black'))
ago_place=[]
has_label=[]
delete_change=[]
all_change={}
old=str(class_size.get())
last_boy=0
last_girl=0
p=0

def scale_process(value):
    global p,label,label_id_all
    if 1 < len(label_id_all):
        if p + 1 > scale_change.get() and not ro_change_place.get():
            p = scale_change.get() - 1
        for key,value in label_id_all.items():
            if key+1 > scale_change.get():
                value.config(fg='black')
                value.place_forget()
            elif key < scale_change.get():
                value.place(x=all_place[key][0],y=all_place[key][1],anchor='center')
    if scale_change.get() == 1:
        for key,value in label_id_all.items():
            value.destroy()
        label_id_all={}
        try:
            label.place(x=389,y=149,anchor='center')
        except tk.TclError as e:
            label = tk.Label(root, text=f"{random_num}",font=('黑体',70),heigh=3,width=11,borderwidth=3,relief="solid")
            label.place(x=389,y=149,anchor='center')
        ro_place.place_forget()
    if int(scale_change.get()) >= 2:
        ro_place.place(x=10,y=84)

scale_change = tk.Scale(root, from_=1, to=15, orient=tk.HORIZONTAL,command=scale_process)
speed = tk.Scale(root, from_=0, to=0.5, orient=tk.HORIZONTAL,resolution=0.01)
all_place=[[195,53],[292,53],[389,53],[486,53],[583,53],[195,149],[292,149],[389,149],[486,149],[583,149],[195,245],[292,245],[389,245],[486,245],[583,245]]
label_id_all={}

class button:
    
    def only():#被按钮调用抽一次的函数
        global random_num,label,p,all_label,id_,label_id_all,n,old,ago_place,last_boy,last_girl
        while '0' in all_label:
            all_label.remove('0')
        while '0' in has_label:
            has_label.remove('0')
        if int(class_size.get()) > int(old):
            add_del.update_checkbox(slider_face)
            slider_face.slider.set(slider_face.slider.get())
            for b in range(int(old)+1,int(class_size.get())+1):
                all_label.append(str(b))
        if int(class_size.get()) < int(old):
            if slider_face.slider.get() > (int(old)-5)*30:
                slider_face.slider.set(slider_face.slider['to'])
            add_del.update_checkbox(slider_face)
            for z in range(int(class_size.get())+1,int(old)+1):
                while str(z) in all_label:
                    del all_label[all_label.index(str(z))]
                while z-1 in all_change:
                    del all_change[z-1]
                while str(z) in has_label:
                    del has_label[has_label.index(str(z))]
        if all_label != []:
            old=str(class_size.get())
        for i in range(int(first_girl.get()),int(class_size.get())):
            if i not in all_change:
                add_del.checkbox = tk.Button(root,width=10, state='normal',text=f'{i+1}',font=('黑体',16,'bold'),bd=0,fg='white',bg='#C0C0C0',command=lambda ordinal=i:add_del.run_add_del(add_del,ordinal))
                all_change[i]=add_del.checkbox
            if EXCLUDE_GIRL.get():
                all_change[i].config(bg='red')
                if str(all_change[i]['text']) in all_label:
                    all_label.remove(str(all_change[i]['text']))
            if i-1 in all_change and all_change[i-1]['bg']=='#C0C0C0' and str(i) not in all_label:
                all_label.append(str(i))
                all_change[i-1].config(bg='red')
        last_girl=int(class_size.get())
        if EXCLUDE_GIRL.get():
            for i in range(int(first_girl.get()),int(class_size.get())+1):
                if i-1 in all_change and all_change[i-1]['bg']=='#C0C0C0' and str(i) not in all_label:
                    all_label.append(str(i))
                all_change[i-1].config(bg='red')
                if all_change[i-1]['bg']=='red' and str(i) in all_label:
                    all_label.remove(str(i))
            if 0 != last_boy < int(first_girl.get()):
                for LD in range(last_boy,int(first_girl.get())+1):
                    all_change[LD-1].config(bg='#C0C0C0')
                    if str(LD)not in all_label:
                        all_label.append(str(LD))
            last_boy=int(first_girl.get())
        elif not EXCLUDE_GIRL.get()and not re_1.get():
            all_label=[str(i) for i in list(range(1,int(class_size.get())+1))]
        if EXCLUDE_BOY.get():
            for i in range(0,int(first_girl.get())-1):
                if i in all_change and all_change[i]['bg']=='#C0C0C0' and str(i+1) not in all_label:
                    all_label.append(str(i+1))
                all_change[i].config(bg='red')
                if all_change[i]['bg']=='red' and str(i+1) in all_label:
                    all_label.remove(str(i+1))
                if str(0) in all_label:
                    all_label.remove(str(0))
        if re_0.get()and re_1.get():
            for m in has_label:
                if m in all_label:
                    all_label.remove(str(m))
                
        if scale_change.get()>=2:
            if p == scale_change.get() and not ro_change_place.get():#懒死我算了
                p-=scale_change.get()
                label_id_all[scale_change.get()-1].config(fg='black')
            elif ro_change_place.get():
                p = random.randint(0,int(scale_change.get())-1)
            label.id = p
            if p > scale_change.get() and not ro_change_place.get():
                p = scale_change.get()-1
            if p in label_id_all:
                label = label_id_all[p]
                label.config(text=f"{random_num}")
            else:
                if len(label_id_all) == 0:
                    label.place_forget()
                label = tk.Label(root, text=f"{random_num}",font=('黑体',70),heigh=1,width=2,borderwidth=1,relief="solid")
                label.place(x=all_place[p][0],y=all_place[p][1],anchor='center')
            label_id_all[p] = label
            if ro_change_place.get() and label_id_all != {} and len(ago_place) >= 1 and ago_place[-1] in label_id_all:
                label_id_all[ago_place[-1]].config(fg='black')
            elif not ro_change_place.get():p+=1
            ago_place.append(p)
            if len(ago_place) > 15:
                del ago_place[0]
            if re_1.get() and label["text"] == "均已\n重复":
                label.config(borderwidth=1,relief="solid",heigh=2,width=4)
            else:
                label.config(borderwidth=1,relief="solid",heigh=1,width=2,fg='#FFDD00')
                if ago_place[-1]-2 > -1 and not ro_change_place.get() and ago_place[-1]-2 in label_id_all:
                    label_id_all[ago_place[-1]-2].config(fg='black')
        else:
            for key,value in label_id_all.items():
                value.destroy()
            if label_id_all != {}:
                label_id_all = {}
            p=0
            label.place(x=389,y=149,anchor='center')
            label.config(text=f"{random_num}",font=('黑体',70),heigh=3,width=11,borderwidth=3,relief="solid")            
        if not re_1.get()or not label["text"]=="均已\n重复":
            label.config(font=('黑体',70))
        if re_1.get():
            check.no_re()
        else:
            for key,value in all_change.items():
                if value['bg']=='red' and str(key+1) in all_label:
                    all_label.remove(str(key+1))
        if not re_1.get():
            random_num=str(random.choice(all_label))
        only_button.config(text='单抽')#改变按钮文本显示
        if re_0.get():
            check.print_re()
        if not re_0.get() and not re_1.get():
            label.config(text=random_num)#刷新显示
        time.sleep(speed.get())
        
    def many_start():
        many_button.config(text="截停",command=button.many_end)
        while many_button["text"]=="截停":
            button.only()
            label.update()
            
    def many_end():
        many_button.config(text="多抽",command=button.many_start)

only_button = tk.Button(root, text="截停",font=('黑体',17,'bold'),command=button.only,width=12,height=3,bg='#c0c0c0',relief=tk.FLAT,bd=0.5,fg="white")  
only_button.place(x=312,y=300)
label0 = tk.Label(root, text="",font=('黑体',10),heigh=1)
len_has=tk.Label(root, text=f"已有数目:{len(set(has_label))}",font=('黑体',15),heigh=1,bg='#F5F5F5')

def init_start():
    while only_button['text']=="截停":
        random_num=str(random.randint(1,39))
        label.config(text=random_num)
        label.update()

class add_del:  
    
    def __init__(self,root):
        self.slider = tk.Scale(root,from_=0, to=30*(int(class_size.get())-5),length=160,showvalue=False,resolution=30,command=self.update_checkbox)
        self.slider.configure(sliderrelief="flat")
        self.slider.place(x=780,y=20)
        for i in range(int(class_size.get())):
            if i not in all_change:
                self.checkbox = tk.Button(root,width=10, state='normal',text=f'{i+1}',font=('黑体',16,'bold'),bd=0,fg='white',bg='#C0C0C0',command=lambda ordinal=i:self.run_add_del(ordinal))
                all_change[i]=self.checkbox
            if  (20+i*30) <= 142 and (20+i*30) > 12:
                all_change[i].place(y=25+i*30, x=652)
            else:
                all_change[i].place_forget()
        self.old=0
        
    def update_checkbox(self,_=None):  
        #更新勾选框
        slider_pos = self.slider.get()
        if int(class_size.get()) < self.old:
            for a in range(int(class_size.get()),self.old):
                if a in all_change:
                    all_change[a].place_forget()
            self.slider.set((int(class_size.get())-5)*30)
        self.old = int(class_size.get())
        self.slider.config(to=(int(class_size.get())-5)*30)
        for i in range(int(class_size.get())):
            if i not in all_change:
                self.checkbox = tk.Button(root,width=10, state='normal',text=f'{i+1}',font=('黑体',16,'bold'),bd=0,fg='white',bg='#C0C0C0',command=lambda ordinal=i:self.run_add_del(ordinal))
                all_change[i]=self.checkbox
                if EXCLUDE_GIRL.get():
                    self.checkbox.config(bg='red')
                    if str(self.checkbox['text']) in all_label:
                        all_label.remove(str(self.checkbox['text']))
            if  (20-slider_pos+i*30) <= 148 and (20-slider_pos+i*30) > 12:
                all_change[i].place(y=25-slider_pos+i*30, x=652)
            else:
                all_change[i].place_forget()
        if EXCLUDE_BOY.get():
            for i in range(int(first_girl.get())-1):
                all_change[i].config(bg='red')
                if str(i) in all_label:
                    all_label.remove(str(i))

    def run_add_del(self,ordinal):
        if all_change[ordinal]['bg']=='#C0C0C0':
            all_change[ordinal].config(bg='red')
            if str(ordinal+1) in all_label:
                all_label.remove(str(ordinal+1))
        elif all_change[ordinal]['bg']=='red':
            all_change[ordinal].config(bg='#C0C0C0')
            if str(ordinal+1) not in all_label:
                all_label.append(str(ordinal+1))
        
init_start()
many_button = tk.Button(root, text="多抽",font=('黑体',17,'bold'), command=button.many_start,width=12 ,height=3,bg='#c0c0c0',relief=tk.FLAT,bd=0.5,fg="white")
many_button.place(x=312,y=400)
slider_face=add_del(root)
slider_face
deleted=[]

class check:
    
    def clear_has():
        global has_label
        has_label=[]
        if re_0.get():
            len_has.config(text=f"已有数目:0")
            len_has.place(x=5,y=5)
        else:
            len_has.place_forget()
            label0.place_forget()
        if re_0.get() and re_1.get():
            for NI in deleted:
                if NI not in has_label:
                    has_label.append(NI)
            len_has.config(text=f"已有数目:{len(set(has_label))}")
            
    def print_re():
        global random_num,label0,has_label
        re_nums=len([x for x,y in enumerate(has_label) if y == random_num])
        if re_0.get()and random_num not in has_label:
            if not re_1.get():
                label.config(text=random_num)
            label0.place_forget()
        elif re_0.get()and random_num in has_label:
            if not re_1.get():
                label.config(text=f"{random_num}")
            label0.config(text=f"(此已重复{re_nums}次)")
            label0.place(x=13,y=30)
        has_label.append(random_num)
        if not re_1.get():
            random_num=str(random.choice(all_label))
        len_has_label=len(set(has_label))
        if '0'in has_label :
            len_has_label-=1
            if not EXCLUDE_BOY.get()and not EXCLUDE_GIRL.get():
                len_has_label+=1
        if len_has_label > int(class_size.get()):
            len_has_label = int(class_size.get())
        len_has.config(text=f"已有数目:{len_has_label}")
        
    def open_all():
        global all_label,deleted
        for key,value in all_change.items():
            if value['bg']=='red' and str(key+1) in all_label:
                all_label.remove(str(key+1))
        if not re_1.get()and deleted != []:
            for i in deleted:
                all_change[int(i)-1].config(bg='#C0C0C0')
            all_label.extend(deleted)
            deleted=[]
        if not re_1.get()and '均' in label['text']:
            all_label=[str(i) for i in list(range(1,int(class_size.get())+1))]
            
    def no_re():
        global all_label,random_num
        while '0' in all_label:
            all_label.remove('0')
        if all_label!=[]:
            random_num=random.choice(all_label)
        if re_1.get()and random_num in all_label:
            all_label.remove(random_num)
            if int(random_num) >= 1:
                all_change[int(random_num)-1].config(bg='red')
            else:
                random_num=random.choice(all_label)
            deleted.append(random_num)
            label.config(text=f"{random_num}")
        elif re_1.get()and all_label==[] and scale_change.get() == 1:
            label.config(text="均已重复")
            random_num='0'
        elif re_1.get()and all_label==[] and scale_change.get() != 1:
            label.config(text="均已\n重复",height=2,width=4,font = ('黑体',34))
            random_num='0'
        elif not re_1.get()and '均' in label['text']:
            all_label=[str(i) for i in list(range(1,int(class_size.get())+1))]
        else:
            label.config(text=f"{random_num}")

class exclude:
    
    def boy():
        global all_label
        if EXCLUDE_BOY.get():
            all_label=[str(i) for i in list(range(int(first_girl.get()),int(class_size.get())+1))]
        elif not EXCLUDE_BOY.get() and not EXCLUDE_GIRL.get():
            all_label=[str(i) for i in list(range(1,int(class_size.get())+1))]
        for B in range(0,int(first_girl.get())-1):
            if EXCLUDE_BOY.get():
                all_change[B].config(bg='red')
                if str(B) in all_label:
                    all_label.remove(str(B)) 
            else:
                all_change[B].config(bg='#C0C0C0')
                if str(B) not in all_label:
                    all_label.append(str(B))
    def girl():
        global all_label
        if EXCLUDE_GIRL.get():
            all_label=[str(i) for i in list(range(1,int(first_girl.get())))]
        elif not EXCLUDE_BOY.get() and not EXCLUDE_GIRL.get():
            all_label=[str(i) for i in list(range(1,int(class_size.get())+1))]
        for G in range(int(first_girl.get()),int(class_size.get())+1):
            if EXCLUDE_GIRL.get():
                try:
                    all_change[G-1].config(bg='red')
                except KeyError as e:
                    print(all_change)
                if str(G) in all_label:
                    all_label.remove(str(G)) 
            else:
                all_change[G-1].config(bg='#C0C0C0')
                if str(G) not in all_label:
                    all_label.append(str(G))

def Negate_command():
    for key,value in all_change.items():
        if value['bg']=='red':
            value.config(bg='#C0C0C0')
            if str(key+1) not in all_label:
                all_label.append(str(key+1))
            while str(key+1) in has_label:
                has_label.remove(str(key+1))
            while '0' in has_label:
                has_label.remove('0')
        else:
            value.config(bg='red')
            if str(key+1) in all_label:
                all_label.remove(str(key+1))
                has_label.append(str(key+1))
                
def count_extract():
    count = 0
    while count <= int(counting_init.get())- 1:
        button.only()
        label.update()
        count += 1
        
def chronograph_extract():
    end = time.time()
    begin = time.time()
    while end - begin < int(chronograph_init.get()):
        button.only()
        label.update()
        end = time.time()
    
print_re_check = tk.Checkbutton(root, text="显示重复", variable=re_0,command=check.clear_has)
no_re_check = tk.Checkbutton(root, text="不再重复", variable=re_1,command=check.open_all)
scale_change.configure(sliderlength=38, troughcolor="#10cf70",sliderrelief="flat")
scale_change.place(x=10,y=234)
speed.configure(sliderlength=38, troughcolor="#148AFF",sliderrelief="flat")
speed.place(x=660,y=234)
speed_label=tk.Label(root, text="变动速率/秒",font=('黑体',10),heigh=1,width=14)
speed_label.place(x=660,y=274)
show_label_max=tk.Label(root, text="罗列上限",font=('黑体',10),heigh=1,width=14)
show_label_max.place(x=10,y=274)
class_size_print.place(x=662,y=182)
class_size.place(x=707,y=186)
first_girl_print.place(x=680,y=210)
first_girl.place(x=665,y=213)
no_re_check.place(x=10,y=174)
print_re_check.place(x=10,y=204)
add_del_print = tk.Label(root, text="手动排除学号",font=('宋体',12),width=17)
add_del_print.place(x=655,y=0)
exclude_boy = tk.Checkbutton(root, text="排除男生", variable=EXCLUDE_BOY,command=exclude.boy)
exclude_boy.place(x=10,y=144)
exclude_girl = tk.Checkbutton(root, text="排除女生", variable=EXCLUDE_GIRL,command=exclude.girl)
exclude_girl.place(x=10,y=114)
Negate=tk.Button(root,text='取 反',font=('黑体',12,'bold'),bd=0,bg='#C1C1C1',fg='white',command=Negate_command)
Negate.place(x=746,y=183)
counting_show=tk.Button(root, text="抽 次",font=('黑体',17,'bold'),width=12 ,height=3,bg='#c0c0c0',relief=tk.FLAT,bd=0.5,fg="white",command=count_extract)
counting_show.place(x=116,y=300)
counting_init=tk.Entry(root,font=('黑体',14),textvariable=tk.StringVar(root,5),width=1,bd=0)
counting_init.place(x=191,y=332)
chronograph_show=tk.Button(root, text="抽 秒",font=('黑体',17,'bold'),width=12 ,height=3,bg='#c0c0c0',relief=tk.FLAT,bd=0.5,fg="white",command=chronograph_extract)
chronograph_show.place(x=116,y=400)
chronograph_init=tk.Entry(root,font=('黑体',14),textvariable=tk.StringVar(root,3),width=1,bd=0)
chronograph_init.place(x=191,y=432)
root.mainloop()
#我感觉我敲的比屎还臭
#臃肿不堪,臭气冲天
#再有下次一定写注释