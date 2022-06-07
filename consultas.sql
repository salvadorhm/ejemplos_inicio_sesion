select usuarios.uid, usuarios.rol, usuarios.email
from usuarios
where usuarios.email="admin@email.com" and usuarios.password="21232f297a57a5a743894a0e4a801fc3" and usuarios.status="activo"
group by usuarios.uid;


select count(usuarios.uid) as auth
from usuarios
where usuarios.email="admin@email8.com" and usuarios.password="21232f297a57a5a743894a0e4a801fc3" and usuarios.status="activo";