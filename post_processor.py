#Author: Su Li
#Date: 2022-11-1
#Function name: plot_1D_results

import pandas as pd
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str):
	if date_str[-8:-6] != '24':
		dt_obj = pd.to_datetime(date_str)
	else:
		date_str = date_str[0:-8] + '00' + date_str[-6:]
		dt_obj = pd.to_datetime(date_str) + dt.timedelta(days = 1)
	return dt_obj

def plot_1D_results(output_path, plot_column_name, y_axis_title, plot_title):
	fig, axs = plt.subplots(1, 1, figsize = (20,10)) #diagram arranged in a row,a column,position
	frontsize = 20
	for i in parameter_key:
		this_path = parameter_key
		this_df = pd.read_csv(this_path)
		this_df['Date/Time'] = '2002' + this_df['Date/Time']
		this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
		data_st_date = this_df.iloc[0]['Date/Time'] #get all the data from 'Date/Time'
		date_ed_date = this_df.iloc[-1]['Date/Time']
		date_list = this_df['Date/Time']
		this_y = this_df[plot_column_name].values
		axs.plot(date_list, this_y, #split canvas drawing
			alpha = 0.7,
			linewidth = 2,
			label = i)
	datetime_ax_loc = mdates.HourLocator() #loc means lines codes
	datetime_ax_fmt = mdates.DateFormatter('%H:%H') #fmt means writes data in various format
	axs.xaxis.set_major_locator(datetime_ax_loc)
	axs.xaxis.set_major_formattter(datetime_ax_fmt)
	for tick in axs.xaxis.get_major_ticks():
		tick.label.set_fontsize(fontsize*0.8)
	for tick in axs.yaxis.get_major_ticks():
		tick.label.set_fontsize(fontsize*0.8)
	axs.tick_params('x', labelrotation = 45)
	axs.set_xlabel('Time(%s to %s)'% (data_st_date, date_ed_date),
				fontsize = fontsize)
	axs.set_ylabel('Indoor Air Temperature (C)',
				fontsize = fontsize)
	axs.legend(fontsize = fontsize)
	plt.savefig('simulation of indoor air temperature vs.SHGC.png')
	plt.show()
