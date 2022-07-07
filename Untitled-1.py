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

task_admins_m = df_may['platform'].value_counts()[0]
task_andr_m = df_may['platform'].value_counts()[1]
task_ios_m = df_may['platform'].value_counts()[2]


diff_1 = task_admins_j - task_admins_m
diff_2 = task_andr_j - task_andr_m
diff_3 = task_ios_j - task_ios_m

# %%
st.title("Отчет UrgY")
st.subheader("Количество созданных задач")

# %%
st.metric(label="Количество созданных задач за июнь", value=all_task_june, delta=difference_task)

# %%
col1, col2, col3, col4 = st.columns(4)
col1.metric("Количество созданных задач за июнь", all_task_june, difference_task)
col2.metric("Количество созданных задач за июнь Android", task_andr_j, diff_2)
col3.metric("Количество созданных задач за июнь iOS", task_ios_j, diff_3)
col4.metric("Количество созданных задач за июнь Admins", task_admins_j,diff_1)


