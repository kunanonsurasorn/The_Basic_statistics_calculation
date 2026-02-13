import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox
from statistics_calculation import statistics_calculation_output
from csv_file_saving import save_statistics_csv
import pandas as pd

#Data for function

filename = ""
df = None
x_columns = ["-"]
y_columns = ["-"]
result_statistics = {"Min":None,"Median":None,"Mean":None,"Max":None,"Range":None,
                     "Standard Deviation":None,"Quartile 1":None,"Quartile 2":None,"Quartile 3":None,"Amount":None}

#Function

def file_import():
    global filename
    filename = filedialog.askopenfilename(title="Import CSV file",filetypes=[("CSV files","*.csv")])
    if filename:
        upload_file_button.config(state="active")

def file_upload():
    global df,x_columns,y_columns

    try:
        df = pd.read_csv(f'{filename}')
    except Exception as e:
        messagebox.showerror("File Error",f"Cannot read file:\n{e}")
        return

    if df is not None:
        upload_file_path_label.config(text=f"{filename}")
        statistics_calculation_button.config(state="active")

    columns_name = list(df.columns)   

    x_columns = columns_name.copy()
    y_columns = columns_name.copy()

    xaxis_columns_option_menu['menu'].delete(0,"end")
    yaxis_columns_option_menu['menu'].delete(0,"end")

    for column in x_columns:
        xaxis_columns_option_menu['menu'].add_command(label=column,command=tk._setit(option_x_axis,column))

    for column in y_columns:
        yaxis_columns_option_menu['menu'].add_command(label=column,command=tk._setit(option_y_axis,column))

    option_x_axis.set(x_columns[0])
    option_y_axis.set(y_columns[0])

def file_calculation():
    global min_df,median_df,mean_df,max_df,range_max_min_df
    global std_df,q1_df,q2_df,q3_df,amount_df
    if df is None:
        messagebox.showwarning("Data Error","No file uploaded")
        return
    
    if option_y_axis.get() not in df.columns:
        messagebox.showwarning("Selection Error","Please select a valid column")
        return
    
    try:
        y = pd.to_numeric(df[option_y_axis.get()],errors='coerce')
        y = y.dropna()

    except Exception as e:
        messagebox.showerror("Column Error",str(e))
        return
    
    if y.empty:
        messagebox.showerror("Data Error","No valid numeric data in selected column")
        return

    try:
        min_df,median_df,mean_df,max_df,range_max_min_df,std_df,q1_df,q2_df,q3_df,amount_df = statistics_calculation_output(y)
    except Exception as e:
        messagebox.showerror("Calculation Error",str(e))
        return
    
    show_result_statistics()

    update_result_statistics()

    save_button.config(state="active")

def show_result_statistics():

    min_output.config(text=min_df)
    median_output.config(text=median_df)
    mean_output.config(text=mean_df)
    max_output.config(text=max_df)
    range_max_min_output.config(text=range_max_min_df)

    standard_deviation_output.config(text=std_df)
    quartile_1_output.config(text=q1_df)
    quartile_2_output.config(text=q2_df)
    quartile_3_output.config(text=q3_df)
    amount_output.config(text=amount_df)

def update_result_statistics():

    result_statistics.update({"Min":float(min_df)})
    result_statistics.update({"Median":float(median_df)})
    result_statistics.update({"Mean":float(mean_df)})
    result_statistics.update({"Max":float(max_df)})
    result_statistics.update({"Range":float(range_max_min_df)})

    result_statistics.update({"Standard Deviation":float(std_df)})
    result_statistics.update({"Quartile 1":float(q1_df)})
    result_statistics.update({"Quartile 2":float(q2_df)})
    result_statistics.update({"Quartile 3":float(q3_df)})
    result_statistics.update({"Amount":int(amount_df)})

def saving_file_statistics():

    csv_filename = str(filename_input_box.get())

    if not csv_filename:
        messagebox.showwarning("Filename Error","Please enter file name")
        return
    
    if not csv_filename.endswith(".csv"):
        csv_filename = csv_filename+".csv"

    try:
        save_statistics_csv(csv_filename,result_statistics)

    except Exception as e:
        messagebox.showerror("Save Error",str(e))
        return

    reset_button.config(state="active")

def reset_process():

    global filename,df,x_columns,y_columns,result_statistics

    filename = ""
    df = None
    x_columns = ["-"]
    y_columns = ["-"]
    result_statistics = {"Min":None,"Median":None,"Mean":None,"Max":None,"Range":None,
                         "Standard Deviation":None,"Quartile 1":None,"Quartile 2":None,"Quartile 3":None,"Amount":None}
    
    upload_file_path_label.configure(text="File Path")

    min_output.configure(text="-")
    median_output.configure(text="-")
    mean_output.configure(text="-")
    max_output.configure(text="-")
    range_max_min_output.configure(text="-")

    standard_deviation_output.configure(text="-")
    quartile_1_output.configure(text="-")
    quartile_2_output.configure(text="-")
    quartile_3_output.configure(text="-")
    amount_output.configure(text="-")

    upload_file_button.config(state="disabled")
    statistics_calculation_button.config(state="disabled")
    save_button.config(state="disabled")
    reset_button.config(state="disabled")

    option_x_axis.set("Select X Variable")
    option_y_axis.set("Select Y Variable")

#Graphical User Interface

main_window = tk.Tk()
main_window.geometry("900x400")
main_window.title("Statistics Analysis")

title_label = tk.Label(main_window,text="Statistics Analysis",font=("Segoe UI",20),anchor="center")
title_label.grid(row=0,column=0,columnspan=10,padx=5,pady=5)

upload_file_label = tk.Label(main_window,text="Upload File",font=("Segoe UI",15))
upload_file_label.grid(row=1,column=0,padx=5,pady=5)

import_file_button = tk.Button(main_window,text = "Search File",font=("Segoe UI",10),command=file_import)
import_file_button.grid(row=2,column=0,padx=5,pady=5)

upload_file_path_label = tk.Label(main_window,text="File Path",font=("Segoe UI",10))
upload_file_path_label.grid(row=2,column=1,columnspan=8,padx=5,pady=5)

upload_file_button = tk.Button(main_window,text = "Upload",font=("Segoe UI",10),command=file_upload,state="disabled")
upload_file_button.grid(row=2,column=9,padx=5,pady=5)

select_columns_label = tk.Label(main_window,text = "Column",font=("Segoe UI",15))
select_columns_label.grid(row=3,column=0,padx=5,pady=5)

option_x_axis = tk.StringVar(main_window)
option_y_axis = tk.StringVar(main_window)

option_x_axis.set("Select X Variable")
option_y_axis.set("Select Y Variable")

xaxis_columns_option_menu = tk.OptionMenu(main_window,option_x_axis,*x_columns)
xaxis_columns_option_menu.grid(row=3,column=1,padx=5,pady=5)

yaxis_columns_option_menu = tk.OptionMenu(main_window,option_y_axis,*y_columns)
yaxis_columns_option_menu.grid(row=3,column=2,padx=5,pady=5)

statistics_label = tk.Label(main_window,text = "Statistics",font=("Segoe UI",15))
statistics_label.grid(row=4,column=0,padx=5,pady=5)

statistics_calculation_button = tk.Button(main_window,text = "Calculation",font=("Segoe UI",10),command=file_calculation,state="disabled")
statistics_calculation_button.grid(row=4,column=1,padx=5,pady=5)

#Min 
min_label = tk.Label(main_window,text = "Min :",font=("Segoe UI",10))
min_label.grid(row=5,column=0,padx=5,pady=5)

min_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
min_output.grid(row=5,column=1,padx=10,pady=10)

#Median
median_label = tk.Label(main_window,text = "Median :",font=("Segoe UI",10))
median_label.grid(row=5,column=2,padx=5,pady=5)

median_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
median_output.grid(row=5,column=3,padx=10,pady=10)

#Mean
mean_label = tk.Label(main_window,text = "Mean :",font=("Segoe UI",10))
mean_label.grid(row=5,column=4,padx=5,pady=5)

mean_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
mean_output.grid(row=5,column=5,padx=10,pady=10)

#Max
max_label = tk.Label(main_window,text = "Max :",font=("Segoe UI",10))
max_label.grid(row=5,column=6,padx=5,pady=5)

max_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
max_output.grid(row=5,column=7,padx=10,pady=10)

#Range
range_max_min_label = tk.Label(main_window,text = "Range :",font=("Segoe UI",10))
range_max_min_label.grid(row=5,column=8,padx=5,pady=5)

range_max_min_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
range_max_min_output.grid(row=5,column=9,padx=10,pady=10)

#Standard Deviation
standard_deviation_label = tk.Label(main_window,text = "Standard Deviation :",font=("Segoe UI",10))
standard_deviation_label.grid(row=6,column=0,padx=5,pady=5)

standard_deviation_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
standard_deviation_output.grid(row=6,column=1,padx=10,pady=10)

#Quartile 1 

quartile_1_label = tk.Label(main_window,text = "Quartile 1  :",font=("Segoe UI",10))
quartile_1_label.grid(row=6,column=2,padx=5,pady=5)

quartile_1_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
quartile_1_output.grid(row=6,column=3,padx=10,pady=10)

#Quartile 2 

quartile_2_label = tk.Label(main_window,text = "Quartile 2  :",font=("Segoe UI",10))
quartile_2_label.grid(row=6,column=4,padx=5,pady=5)

quartile_2_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
quartile_2_output.grid(row=6,column=5,padx=10,pady=10)

#Quartile 3 

quartile_3_label = tk.Label(main_window,text = "Quartile 3  :",font=("Segoe UI",10))
quartile_3_label.grid(row=6,column=6,padx=5,pady=5)

quartile_3_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
quartile_3_output.grid(row=6,column=7,padx=10,pady=10)

#Amount

amount_label = tk.Label(main_window,text = "Amount  :",font=("Segoe UI",10))
amount_label.grid(row=6,column=8,padx=5,pady=5)

amount_output = tk.Label(main_window,text = "-",font=("Segoe UI",10))
amount_output.grid(row=6,column=9,padx=10,pady=10)

#Saving File

saving_file_label = tk.Label(main_window, text = "Print File name as filename.csv")
saving_file_label.grid(row = 7, column = 0,padx=5,pady=5)

filename_input_box = (tk.Entry(main_window))
filename_input_box.grid(row = 8, column = 0,padx=5,pady=5)

save_button = tk.Button(main_window,text = "Save",font=("Segoe UI",10),command=saving_file_statistics,state="disabled")
save_button.grid(row=8,column=1,padx=5,pady=5)

#Reset

reset_button = tk.Button(main_window,text = "Reset",font=("Segoe UI",10),command=reset_process,state="disabled")
reset_button.grid(row=8,column=2,padx=5,pady=5)

main_window.mainloop()