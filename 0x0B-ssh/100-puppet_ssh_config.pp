# set up my client SSH configuration

file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => "    IdentityFile ~/.ssh/holberton\n
      PasswordAuthentication no\n",
}
