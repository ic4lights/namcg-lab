$procs = Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
  Where-Object { $_.CommandLine -like '*ghost_linearization_125b*' }
foreach ($p in $procs) { Write-Output ("kill " + $p.ProcessId); Stop-Process -Id $p.ProcessId -Force }
if (-not $procs) { Write-Output "none running" }
