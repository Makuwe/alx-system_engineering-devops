#fix nginx to accept and serve more requests

exec {'modify max open files limit setting':
command => 'sed -i "s/4096/15/" /etc/default/nginx && sudo service nginx restart',
path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}