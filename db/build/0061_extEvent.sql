CREATE EVENT SESSION [opediaExEv] ON SERVER 
ADD EVENT sqlserver.existing_connection(
    ACTION(sqlos.task_time,sqlserver.client_hostname,sqlserver.is_system,sqlserver.nt_username,sqlserver.session_server_principal_name,sqlserver.sql_text)
    WHERE ([sqlserver].[database_name]=N'Opedia')),
ADD EVENT sqlserver.login(
    ACTION(sqlos.task_time,sqlserver.client_hostname,sqlserver.is_system,sqlserver.nt_username,sqlserver.session_server_principal_name,sqlserver.sql_text)
    WHERE ([sqlserver].[database_name]=N'Opedia')),
ADD EVENT sqlserver.logout(
    ACTION(sqlos.task_time,sqlserver.client_hostname,sqlserver.is_system,sqlserver.nt_username,sqlserver.session_server_principal_name,sqlserver.sql_text)
    WHERE ([sqlserver].[database_name]=N'Opedia')),
ADD EVENT sqlserver.rpc_completed(SET collect_data_stream=(1)
    ACTION(sqlos.task_time,sqlserver.client_hostname,sqlserver.database_id,sqlserver.database_name,sqlserver.is_system,sqlserver.nt_username,sqlserver.server_principal_name,sqlserver.session_id,sqlserver.session_server_principal_name,sqlserver.sql_text)
    WHERE ((([package0].[greater_than_uint64]([sqlserver].[database_id],(4))) AND ([package0].[equal_boolean]([sqlserver].[is_system],(0)))) AND ([sqlserver].[database_name]=N'Opedia'))),
ADD EVENT sqlserver.sp_statement_completed(
    ACTION(sqlos.task_time,sqlserver.client_hostname,sqlserver.database_id,sqlserver.database_name,sqlserver.is_system,sqlserver.nt_username,sqlserver.server_principal_name,sqlserver.session_id,sqlserver.session_server_principal_name,sqlserver.sql_text)
    WHERE ((([package0].[greater_than_uint64]([sqlserver].[database_id],(4))) AND ([package0].[equal_boolean]([sqlserver].[is_system],(0)))) AND ([sqlserver].[database_name]=N'Opedia'))),
ADD EVENT sqlserver.sql_batch_completed(
    ACTION(sqlos.task_time,sqlserver.client_hostname,sqlserver.database_id,sqlserver.database_name,sqlserver.is_system,sqlserver.nt_username,sqlserver.server_principal_name,sqlserver.session_id,sqlserver.session_server_principal_name,sqlserver.sql_text)
    WHERE ((([package0].[greater_than_uint64]([sqlserver].[database_id],(4))) AND ([package0].[equal_boolean]([sqlserver].[is_system],(0)))) AND ([sqlserver].[database_name]=N'Opedia')))
ADD TARGET package0.event_file(SET filename=N'H:\opediaExEv.xel',max_file_size=(10240))
WITH (MAX_MEMORY=4096 KB,EVENT_RETENTION_MODE=ALLOW_SINGLE_EVENT_LOSS,MAX_DISPATCH_LATENCY=30 SECONDS,MAX_EVENT_SIZE=0 KB,MEMORY_PARTITION_MODE=NONE,TRACK_CAUSALITY=ON,STARTUP_STATE=ON)
GO


