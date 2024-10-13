import os
from RsLogMod.rlog import rlog
from RsLogMod.bin.rslogmod import Configure

Configure.enable_verbose(False)
Configure.enable_log_rotation(True)
Configure.set_log_file_max_size(0.01)
Configure.set_archive_path('archive')
Configure.set_log_folder_path('logs')

if not os.path.exists('logs'):
    os.makedirs('logs')

if not os.path.exists('archive'):
    os.makedirs('archive')


def check_log_rotation():
    archive_logs = os.listdir('archive')
    return len(archive_logs) > 0


try:
    log_batch_size = 10
    total_batches = 2

    for batch in range(total_batches):
        for i in range(log_batch_size):
            rlog(log_file_name='test', log_level=1, log_entry=f'Test entry {i + batch * log_batch_size}')

        if check_log_rotation():
            exit(0)

    exit(1)

except Exception as e:
    exit(1)
