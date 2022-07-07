# %%
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# %%
count_task = "offers_statuses (3).txt"

# %%
df = pd.read_csv(count_task, sep='|')

# %%
df = df.dropna()

df.columns = ['offer_id', 'offer_created_at','platform','count_responds', 'count_prematch']

df['offer_created_at'] = pd.to_datetime(df['offer_created_at'])
df.offer_created_at = df.offer_created_at.values.astype('M8[D]')

df['count_responds'] = df['count_responds'].astype(int)
df['count_prematch'] = df['count_prematch'].astype(int)

df['platform'] = df['platform'].str.strip()

# %%
df_june = df[df['offer_created_at'] > '2022-05-31']
df_may = df[df['offer_created_at'] < '2022-05-31']
##

# %%
all_task_june = df_june['offer_id'].nunique()
all_task_may = df_may['offer_id'].nunique()

difference_task = all_task_june - all_task_may

# %%
task_mobile_may = df_may.query('platform == "android"').count()[0] + df_may.query('platform == "ios"').count()[0]
task_mobile_june = df_june.query('platform == "android"').count()[0] + df_june.query('platform == "ios"').count()[0]

# %%
create_task_mobile_may = task_mobile_may * 100 / all_task_may
create_task_mobile_june = task_mobile_june * 100 / all_task_may

# %%


# %%


# %%


# %%


# %%


# %%
st.title("Отчет UrgY")
st.subheader("Количество созданных задач")

# %%
st.metric(label="Количество созданных задач за июнь", value=all_task_june, delta=difference_task)

# %%
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

# %%



