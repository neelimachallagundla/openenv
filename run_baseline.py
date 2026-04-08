from env_email import EmailEnv, Action as EmailAction
from env_data import DataEnv, Action as DataAction
from env_code import CodeEnv, Action as CodeAction

# Email
email_env = EmailEnv()
obs = email_env.reset()
obs, r1, _, _ = email_env.step(EmailAction(action_type="mark_urgent", target="URGENT: Server down"))

# Data
data_env = DataEnv()
obs = data_env.reset()
obs, r2, _, _ = data_env.step(DataAction(cleaned_data=[1,2]))

# Code
code_env = CodeEnv()
obs = code_env.reset()
obs, r3, _, _ = code_env.step(CodeAction(issues=["null_pointer","unused_variable"]))

total = r1 + r2 + r3
print("Total Reward:", total)
