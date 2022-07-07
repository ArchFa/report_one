# %%
import pandas as pd
import streamlit as st

# %%
count_task = "offers_statuses (3).txt"

# %%
df = pd.read_csv(count_task, sep='|')
#df = pd.read_csv('/Users/arturfattahov/Downloads/Telegram Desktop/offers_statuses (3).txt', sep='|')

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
task_admins_j = df_june['platform'].value_counts()[0]
task_andr_j = df_june['platform'].value_counts()[1]
task_ios_j = df_june['platform'].value_counts()[2]

# %%
st.title("Отчет UrgY")
st.subheader("Количество созданных задач")

# %%
col1, col2, col3, col4 = st.columns(4)
col1.metric("All", all_task_june, difference_task)
col2.metric("Android", task_andr_j, "10")
col3.metric("iOS", task_ios_j, "-21")
col4.metric("Admins", task_admins_j, "-261")

# %%
st.subheader("Процент задач создаваемых через приложение")

# %%
st.metric(label="Процент задач через приложения", value="2.12%", delta="-0.25%")

# %%
st.subheader("Общее количество откликов на все задачи за месяц")

# %%
st.metric(label="Процент задач через приложения", value="25540", delta="2338")

# %%
st.subheader("Общее количество прематчей на все задачи за месяц")

# %%
st.metric(label="Процент задач через приложения", value="25164", delta="2372")

# %%



