class Triangle:
     pass

class Circle:
     pass

def triangle_perimeter(t):
    if isinstance(t, Triangle):
        if t.s1 > 0 and t.s2 > 0 and t.s3 > 0 and \
           t.s1 + t.s2 > t.s3 and \
           t.s2 + t.s3 > t.s1 and \
           t.s1 + t.s3 > t.s2:
            return t.s1 + t.s2 + t.s3
    