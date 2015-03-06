## 1. jquery 2.1.1 not support Firefox3.5/3.6
  but jquery1.11.2 is available

## manytomanyField add

```
users = User.objects.all()
p1.members.add()
```
will raise error like TypeError: int() argument must be a string or a number, not 'QuerySet'
should add one by one like this

```
users = User.objects.all()
for user in users
    p1.members.add(user)
```

##  manytomanyField  read out
```
class Project(models.Model):
    name  = models.CharField(max_length=400)
    members = models.ManyToManyField(User,related_name="project_members")

p1 = Project.objects.all()[0]
print p1.members.all()
```
