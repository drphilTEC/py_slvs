# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_slvs', [dirname(__file__)])
        except ImportError:
            import _slvs
            return _slvs
        if fp is not None:
            try:
                _mod = imp.load_module('_slvs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _slvs = swig_import_helper()
    del swig_import_helper
else:
    import _slvs
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_slvs.SLVS_FREE_IN_3D_swigconstant(_slvs)
SLVS_FREE_IN_3D = _slvs.SLVS_FREE_IN_3D
class param(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, param, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, param, name)
    __repr__ = _swig_repr
    __swig_setmethods__["h"] = _slvs.param_h_set
    __swig_getmethods__["h"] = _slvs.param_h_get
    if _newclass:
        h = _swig_property(_slvs.param_h_get, _slvs.param_h_set)
    __swig_setmethods__["group"] = _slvs.param_group_set
    __swig_getmethods__["group"] = _slvs.param_group_get
    if _newclass:
        group = _swig_property(_slvs.param_group_get, _slvs.param_group_set)
    __swig_setmethods__["val"] = _slvs.param_val_set
    __swig_getmethods__["val"] = _slvs.param_val_get
    if _newclass:
        val = _swig_property(_slvs.param_val_get, _slvs.param_val_set)

    def __init__(self):
        this = _slvs.new_param()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _slvs.delete_param
    __del__ = lambda self: None
param_swigregister = _slvs.param_swigregister
param_swigregister(param)


_slvs.SLVS_E_POINT_IN_3D_swigconstant(_slvs)
SLVS_E_POINT_IN_3D = _slvs.SLVS_E_POINT_IN_3D

_slvs.SLVS_E_POINT_IN_2D_swigconstant(_slvs)
SLVS_E_POINT_IN_2D = _slvs.SLVS_E_POINT_IN_2D

_slvs.SLVS_E_NORMAL_IN_3D_swigconstant(_slvs)
SLVS_E_NORMAL_IN_3D = _slvs.SLVS_E_NORMAL_IN_3D

_slvs.SLVS_E_NORMAL_IN_2D_swigconstant(_slvs)
SLVS_E_NORMAL_IN_2D = _slvs.SLVS_E_NORMAL_IN_2D

_slvs.SLVS_E_DISTANCE_swigconstant(_slvs)
SLVS_E_DISTANCE = _slvs.SLVS_E_DISTANCE

_slvs.SLVS_E_WORKPLANE_swigconstant(_slvs)
SLVS_E_WORKPLANE = _slvs.SLVS_E_WORKPLANE

_slvs.SLVS_E_LINE_SEGMENT_swigconstant(_slvs)
SLVS_E_LINE_SEGMENT = _slvs.SLVS_E_LINE_SEGMENT

_slvs.SLVS_E_CUBIC_swigconstant(_slvs)
SLVS_E_CUBIC = _slvs.SLVS_E_CUBIC

_slvs.SLVS_E_CIRCLE_swigconstant(_slvs)
SLVS_E_CIRCLE = _slvs.SLVS_E_CIRCLE

_slvs.SLVS_E_ARC_OF_CIRCLE_swigconstant(_slvs)
SLVS_E_ARC_OF_CIRCLE = _slvs.SLVS_E_ARC_OF_CIRCLE

_slvs.SLVS_E_TRANSFORM_swigconstant(_slvs)
SLVS_E_TRANSFORM = _slvs.SLVS_E_TRANSFORM
class entity(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, entity, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, entity, name)
    __repr__ = _swig_repr
    __swig_setmethods__["h"] = _slvs.entity_h_set
    __swig_getmethods__["h"] = _slvs.entity_h_get
    if _newclass:
        h = _swig_property(_slvs.entity_h_get, _slvs.entity_h_set)
    __swig_setmethods__["group"] = _slvs.entity_group_set
    __swig_getmethods__["group"] = _slvs.entity_group_get
    if _newclass:
        group = _swig_property(_slvs.entity_group_get, _slvs.entity_group_set)
    __swig_setmethods__["type"] = _slvs.entity_type_set
    __swig_getmethods__["type"] = _slvs.entity_type_get
    if _newclass:
        type = _swig_property(_slvs.entity_type_get, _slvs.entity_type_set)
    __swig_setmethods__["wrkpl"] = _slvs.entity_wrkpl_set
    __swig_getmethods__["wrkpl"] = _slvs.entity_wrkpl_get
    if _newclass:
        wrkpl = _swig_property(_slvs.entity_wrkpl_get, _slvs.entity_wrkpl_set)
    __swig_setmethods__["point"] = _slvs.entity_point_set
    __swig_getmethods__["point"] = _slvs.entity_point_get
    if _newclass:
        point = _swig_property(_slvs.entity_point_get, _slvs.entity_point_set)
    __swig_setmethods__["normal"] = _slvs.entity_normal_set
    __swig_getmethods__["normal"] = _slvs.entity_normal_get
    if _newclass:
        normal = _swig_property(_slvs.entity_normal_get, _slvs.entity_normal_set)
    __swig_setmethods__["distance"] = _slvs.entity_distance_set
    __swig_getmethods__["distance"] = _slvs.entity_distance_get
    if _newclass:
        distance = _swig_property(_slvs.entity_distance_get, _slvs.entity_distance_set)
    __swig_setmethods__["param"] = _slvs.entity_param_set
    __swig_getmethods__["param"] = _slvs.entity_param_get
    if _newclass:
        param = _swig_property(_slvs.entity_param_get, _slvs.entity_param_set)
    __swig_setmethods__["src"] = _slvs.entity_src_set
    __swig_getmethods__["src"] = _slvs.entity_src_get
    if _newclass:
        src = _swig_property(_slvs.entity_src_get, _slvs.entity_src_set)
    __swig_setmethods__["scale"] = _slvs.entity_scale_set
    __swig_getmethods__["scale"] = _slvs.entity_scale_get
    if _newclass:
        scale = _swig_property(_slvs.entity_scale_get, _slvs.entity_scale_set)
    __swig_setmethods__["timesApplied"] = _slvs.entity_timesApplied_set
    __swig_getmethods__["timesApplied"] = _slvs.entity_timesApplied_get
    if _newclass:
        timesApplied = _swig_property(_slvs.entity_timesApplied_get, _slvs.entity_timesApplied_set)
    __swig_setmethods__["asTrans"] = _slvs.entity_asTrans_set
    __swig_getmethods__["asTrans"] = _slvs.entity_asTrans_get
    if _newclass:
        asTrans = _swig_property(_slvs.entity_asTrans_get, _slvs.entity_asTrans_set)
    __swig_setmethods__["asAxisAngle"] = _slvs.entity_asAxisAngle_set
    __swig_getmethods__["asAxisAngle"] = _slvs.entity_asAxisAngle_get
    if _newclass:
        asAxisAngle = _swig_property(_slvs.entity_asAxisAngle_get, _slvs.entity_asAxisAngle_set)

    def __init__(self):
        this = _slvs.new_entity()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _slvs.delete_entity
    __del__ = lambda self: None
entity_swigregister = _slvs.entity_swigregister
entity_swigregister(entity)


_slvs.SLVS_C_POINTS_COINCIDENT_swigconstant(_slvs)
SLVS_C_POINTS_COINCIDENT = _slvs.SLVS_C_POINTS_COINCIDENT

_slvs.SLVS_C_PT_PT_DISTANCE_swigconstant(_slvs)
SLVS_C_PT_PT_DISTANCE = _slvs.SLVS_C_PT_PT_DISTANCE

_slvs.SLVS_C_PT_PLANE_DISTANCE_swigconstant(_slvs)
SLVS_C_PT_PLANE_DISTANCE = _slvs.SLVS_C_PT_PLANE_DISTANCE

_slvs.SLVS_C_PT_LINE_DISTANCE_swigconstant(_slvs)
SLVS_C_PT_LINE_DISTANCE = _slvs.SLVS_C_PT_LINE_DISTANCE

_slvs.SLVS_C_PT_FACE_DISTANCE_swigconstant(_slvs)
SLVS_C_PT_FACE_DISTANCE = _slvs.SLVS_C_PT_FACE_DISTANCE

_slvs.SLVS_C_PT_IN_PLANE_swigconstant(_slvs)
SLVS_C_PT_IN_PLANE = _slvs.SLVS_C_PT_IN_PLANE

_slvs.SLVS_C_PT_ON_LINE_swigconstant(_slvs)
SLVS_C_PT_ON_LINE = _slvs.SLVS_C_PT_ON_LINE

_slvs.SLVS_C_PT_ON_FACE_swigconstant(_slvs)
SLVS_C_PT_ON_FACE = _slvs.SLVS_C_PT_ON_FACE

_slvs.SLVS_C_EQUAL_LENGTH_LINES_swigconstant(_slvs)
SLVS_C_EQUAL_LENGTH_LINES = _slvs.SLVS_C_EQUAL_LENGTH_LINES

_slvs.SLVS_C_LENGTH_RATIO_swigconstant(_slvs)
SLVS_C_LENGTH_RATIO = _slvs.SLVS_C_LENGTH_RATIO

_slvs.SLVS_C_EQ_LEN_PT_LINE_D_swigconstant(_slvs)
SLVS_C_EQ_LEN_PT_LINE_D = _slvs.SLVS_C_EQ_LEN_PT_LINE_D

_slvs.SLVS_C_EQ_PT_LN_DISTANCES_swigconstant(_slvs)
SLVS_C_EQ_PT_LN_DISTANCES = _slvs.SLVS_C_EQ_PT_LN_DISTANCES

_slvs.SLVS_C_EQUAL_ANGLE_swigconstant(_slvs)
SLVS_C_EQUAL_ANGLE = _slvs.SLVS_C_EQUAL_ANGLE

_slvs.SLVS_C_EQUAL_LINE_ARC_LEN_swigconstant(_slvs)
SLVS_C_EQUAL_LINE_ARC_LEN = _slvs.SLVS_C_EQUAL_LINE_ARC_LEN

_slvs.SLVS_C_SYMMETRIC_swigconstant(_slvs)
SLVS_C_SYMMETRIC = _slvs.SLVS_C_SYMMETRIC

_slvs.SLVS_C_SYMMETRIC_HORIZ_swigconstant(_slvs)
SLVS_C_SYMMETRIC_HORIZ = _slvs.SLVS_C_SYMMETRIC_HORIZ

_slvs.SLVS_C_SYMMETRIC_VERT_swigconstant(_slvs)
SLVS_C_SYMMETRIC_VERT = _slvs.SLVS_C_SYMMETRIC_VERT

_slvs.SLVS_C_SYMMETRIC_LINE_swigconstant(_slvs)
SLVS_C_SYMMETRIC_LINE = _slvs.SLVS_C_SYMMETRIC_LINE

_slvs.SLVS_C_AT_MIDPOINT_swigconstant(_slvs)
SLVS_C_AT_MIDPOINT = _slvs.SLVS_C_AT_MIDPOINT

_slvs.SLVS_C_HORIZONTAL_swigconstant(_slvs)
SLVS_C_HORIZONTAL = _slvs.SLVS_C_HORIZONTAL

_slvs.SLVS_C_VERTICAL_swigconstant(_slvs)
SLVS_C_VERTICAL = _slvs.SLVS_C_VERTICAL

_slvs.SLVS_C_DIAMETER_swigconstant(_slvs)
SLVS_C_DIAMETER = _slvs.SLVS_C_DIAMETER

_slvs.SLVS_C_PT_ON_CIRCLE_swigconstant(_slvs)
SLVS_C_PT_ON_CIRCLE = _slvs.SLVS_C_PT_ON_CIRCLE

_slvs.SLVS_C_SAME_ORIENTATION_swigconstant(_slvs)
SLVS_C_SAME_ORIENTATION = _slvs.SLVS_C_SAME_ORIENTATION

_slvs.SLVS_C_ANGLE_swigconstant(_slvs)
SLVS_C_ANGLE = _slvs.SLVS_C_ANGLE

_slvs.SLVS_C_PARALLEL_swigconstant(_slvs)
SLVS_C_PARALLEL = _slvs.SLVS_C_PARALLEL

_slvs.SLVS_C_PERPENDICULAR_swigconstant(_slvs)
SLVS_C_PERPENDICULAR = _slvs.SLVS_C_PERPENDICULAR

_slvs.SLVS_C_ARC_LINE_TANGENT_swigconstant(_slvs)
SLVS_C_ARC_LINE_TANGENT = _slvs.SLVS_C_ARC_LINE_TANGENT

_slvs.SLVS_C_CUBIC_LINE_TANGENT_swigconstant(_slvs)
SLVS_C_CUBIC_LINE_TANGENT = _slvs.SLVS_C_CUBIC_LINE_TANGENT

_slvs.SLVS_C_EQUAL_RADIUS_swigconstant(_slvs)
SLVS_C_EQUAL_RADIUS = _slvs.SLVS_C_EQUAL_RADIUS

_slvs.SLVS_C_PROJ_PT_DISTANCE_swigconstant(_slvs)
SLVS_C_PROJ_PT_DISTANCE = _slvs.SLVS_C_PROJ_PT_DISTANCE

_slvs.SLVS_C_WHERE_DRAGGED_swigconstant(_slvs)
SLVS_C_WHERE_DRAGGED = _slvs.SLVS_C_WHERE_DRAGGED

_slvs.SLVS_C_CURVE_CURVE_TANGENT_swigconstant(_slvs)
SLVS_C_CURVE_CURVE_TANGENT = _slvs.SLVS_C_CURVE_CURVE_TANGENT

_slvs.SLVS_C_LENGTH_DIFFERENCE_swigconstant(_slvs)
SLVS_C_LENGTH_DIFFERENCE = _slvs.SLVS_C_LENGTH_DIFFERENCE
class constraint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, constraint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, constraint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["h"] = _slvs.constraint_h_set
    __swig_getmethods__["h"] = _slvs.constraint_h_get
    if _newclass:
        h = _swig_property(_slvs.constraint_h_get, _slvs.constraint_h_set)
    __swig_setmethods__["group"] = _slvs.constraint_group_set
    __swig_getmethods__["group"] = _slvs.constraint_group_get
    if _newclass:
        group = _swig_property(_slvs.constraint_group_get, _slvs.constraint_group_set)
    __swig_setmethods__["type"] = _slvs.constraint_type_set
    __swig_getmethods__["type"] = _slvs.constraint_type_get
    if _newclass:
        type = _swig_property(_slvs.constraint_type_get, _slvs.constraint_type_set)
    __swig_setmethods__["wrkpl"] = _slvs.constraint_wrkpl_set
    __swig_getmethods__["wrkpl"] = _slvs.constraint_wrkpl_get
    if _newclass:
        wrkpl = _swig_property(_slvs.constraint_wrkpl_get, _slvs.constraint_wrkpl_set)
    __swig_setmethods__["valA"] = _slvs.constraint_valA_set
    __swig_getmethods__["valA"] = _slvs.constraint_valA_get
    if _newclass:
        valA = _swig_property(_slvs.constraint_valA_get, _slvs.constraint_valA_set)
    __swig_setmethods__["ptA"] = _slvs.constraint_ptA_set
    __swig_getmethods__["ptA"] = _slvs.constraint_ptA_get
    if _newclass:
        ptA = _swig_property(_slvs.constraint_ptA_get, _slvs.constraint_ptA_set)
    __swig_setmethods__["ptB"] = _slvs.constraint_ptB_set
    __swig_getmethods__["ptB"] = _slvs.constraint_ptB_get
    if _newclass:
        ptB = _swig_property(_slvs.constraint_ptB_get, _slvs.constraint_ptB_set)
    __swig_setmethods__["entityA"] = _slvs.constraint_entityA_set
    __swig_getmethods__["entityA"] = _slvs.constraint_entityA_get
    if _newclass:
        entityA = _swig_property(_slvs.constraint_entityA_get, _slvs.constraint_entityA_set)
    __swig_setmethods__["entityB"] = _slvs.constraint_entityB_set
    __swig_getmethods__["entityB"] = _slvs.constraint_entityB_get
    if _newclass:
        entityB = _swig_property(_slvs.constraint_entityB_get, _slvs.constraint_entityB_set)
    __swig_setmethods__["entityC"] = _slvs.constraint_entityC_set
    __swig_getmethods__["entityC"] = _slvs.constraint_entityC_get
    if _newclass:
        entityC = _swig_property(_slvs.constraint_entityC_get, _slvs.constraint_entityC_set)
    __swig_setmethods__["entityD"] = _slvs.constraint_entityD_set
    __swig_getmethods__["entityD"] = _slvs.constraint_entityD_get
    if _newclass:
        entityD = _swig_property(_slvs.constraint_entityD_get, _slvs.constraint_entityD_set)
    __swig_setmethods__["other"] = _slvs.constraint_other_set
    __swig_getmethods__["other"] = _slvs.constraint_other_get
    if _newclass:
        other = _swig_property(_slvs.constraint_other_get, _slvs.constraint_other_set)
    __swig_setmethods__["other2"] = _slvs.constraint_other2_set
    __swig_getmethods__["other2"] = _slvs.constraint_other2_get
    if _newclass:
        other2 = _swig_property(_slvs.constraint_other2_get, _slvs.constraint_other2_set)

    def __init__(self):
        this = _slvs.new_constraint()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _slvs.delete_constraint
    __del__ = lambda self: None
constraint_swigregister = _slvs.constraint_swigregister
constraint_swigregister(constraint)


def quaternionU(qw, qx, qy, qz):
    return _slvs.quaternionU(qw, qx, qy, qz)
quaternionU = _slvs.quaternionU

def quaternionV(qw, qx, qy, qz):
    return _slvs.quaternionV(qw, qx, qy, qz)
quaternionV = _slvs.quaternionV

def quaternionN(qw, qx, qy, qz):
    return _slvs.quaternionN(qw, qx, qy, qz)
quaternionN = _slvs.quaternionN

def makeQuaternion(ux, uy, uz, vx, vy, vz):
    return _slvs.makeQuaternion(ux, uy, uz, vx, vy, vz)
makeQuaternion = _slvs.makeQuaternion

def makeParam(h, group, val):
    return _slvs.makeParam(h, group, val)
makeParam = _slvs.makeParam

def makePoint2d(h, group, wrkpl, u, v):
    return _slvs.makePoint2d(h, group, wrkpl, u, v)
makePoint2d = _slvs.makePoint2d

def makePoint3d(h, group, x, y, z):
    return _slvs.makePoint3d(h, group, x, y, z)
makePoint3d = _slvs.makePoint3d

def makeNormal3d(h, group, qw, qx, qy, qz):
    return _slvs.makeNormal3d(h, group, qw, qx, qy, qz)
makeNormal3d = _slvs.makeNormal3d

def makeNormal2d(h, group, wrkpl):
    return _slvs.makeNormal2d(h, group, wrkpl)
makeNormal2d = _slvs.makeNormal2d

def makeDistance(h, group, wrkpl, d):
    return _slvs.makeDistance(h, group, wrkpl, d)
makeDistance = _slvs.makeDistance

def makeLineSegment(h, group, wrkpl, ptA, ptB):
    return _slvs.makeLineSegment(h, group, wrkpl, ptA, ptB)
makeLineSegment = _slvs.makeLineSegment

def makeCubic(h, group, wrkpl, pt0, pt1, pt2, pt3):
    return _slvs.makeCubic(h, group, wrkpl, pt0, pt1, pt2, pt3)
makeCubic = _slvs.makeCubic

def makeArcOfCircle(h, group, wrkpl, normal, center, start, end):
    return _slvs.makeArcOfCircle(h, group, wrkpl, normal, center, start, end)
makeArcOfCircle = _slvs.makeArcOfCircle

def makeCircle(h, group, wrkpl, center, normal, radius):
    return _slvs.makeCircle(h, group, wrkpl, center, normal, radius)
makeCircle = _slvs.makeCircle

def makeWorkplane(h, group, origin, normal):
    return _slvs.makeWorkplane(h, group, origin, normal)
makeWorkplane = _slvs.makeWorkplane

def makeTransform(h, group, src, dx, dy, dz, qw, qx, qy, qz, asTrans, asAxisAngle, scale, timesApplied):
    return _slvs.makeTransform(h, group, src, dx, dy, dz, qw, qx, qy, qz, asTrans, asAxisAngle, scale, timesApplied)
makeTransform = _slvs.makeTransform

def makeConstraint(h, group, type, wrkpl, valA, ptA, ptB, entityA, entityB):
    return _slvs.makeConstraint(h, group, type, wrkpl, valA, ptA, ptB, entityA, entityB)
makeConstraint = _slvs.makeConstraint
class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _slvs.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _slvs.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _slvs.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _slvs.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _slvs.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _slvs.SwigPyIterator_equal(self, x)

    def copy(self):
        return _slvs.SwigPyIterator_copy(self)

    def next(self):
        return _slvs.SwigPyIterator_next(self)

    def __next__(self):
        return _slvs.SwigPyIterator___next__(self)

    def previous(self):
        return _slvs.SwigPyIterator_previous(self)

    def advance(self, n):
        return _slvs.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _slvs.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _slvs.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _slvs.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _slvs.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _slvs.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _slvs.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _slvs.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Vec_hConstraint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vec_hConstraint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vec_hConstraint, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _slvs.Vec_hConstraint_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _slvs.Vec_hConstraint___nonzero__(self)

    def __bool__(self):
        return _slvs.Vec_hConstraint___bool__(self)

    def __len__(self):
        return _slvs.Vec_hConstraint___len__(self)

    def __getslice__(self, i, j):
        return _slvs.Vec_hConstraint___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _slvs.Vec_hConstraint___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _slvs.Vec_hConstraint___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _slvs.Vec_hConstraint___delitem__(self, *args)

    def __getitem__(self, *args):
        return _slvs.Vec_hConstraint___getitem__(self, *args)

    def __setitem__(self, *args):
        return _slvs.Vec_hConstraint___setitem__(self, *args)

    def pop(self):
        return _slvs.Vec_hConstraint_pop(self)

    def append(self, x):
        return _slvs.Vec_hConstraint_append(self, x)

    def empty(self):
        return _slvs.Vec_hConstraint_empty(self)

    def size(self):
        return _slvs.Vec_hConstraint_size(self)

    def swap(self, v):
        return _slvs.Vec_hConstraint_swap(self, v)

    def begin(self):
        return _slvs.Vec_hConstraint_begin(self)

    def end(self):
        return _slvs.Vec_hConstraint_end(self)

    def rbegin(self):
        return _slvs.Vec_hConstraint_rbegin(self)

    def rend(self):
        return _slvs.Vec_hConstraint_rend(self)

    def clear(self):
        return _slvs.Vec_hConstraint_clear(self)

    def get_allocator(self):
        return _slvs.Vec_hConstraint_get_allocator(self)

    def pop_back(self):
        return _slvs.Vec_hConstraint_pop_back(self)

    def erase(self, *args):
        return _slvs.Vec_hConstraint_erase(self, *args)

    def __init__(self, *args):
        this = _slvs.new_Vec_hConstraint(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _slvs.Vec_hConstraint_push_back(self, x)

    def front(self):
        return _slvs.Vec_hConstraint_front(self)

    def back(self):
        return _slvs.Vec_hConstraint_back(self)

    def assign(self, n, x):
        return _slvs.Vec_hConstraint_assign(self, n, x)

    def resize(self, *args):
        return _slvs.Vec_hConstraint_resize(self, *args)

    def insert(self, *args):
        return _slvs.Vec_hConstraint_insert(self, *args)

    def reserve(self, n):
        return _slvs.Vec_hConstraint_reserve(self, n)

    def capacity(self):
        return _slvs.Vec_hConstraint_capacity(self)
    __swig_destroy__ = _slvs.delete_Vec_hConstraint
    __del__ = lambda self: None
Vec_hConstraint_swigregister = _slvs.Vec_hConstraint_swigregister
Vec_hConstraint_swigregister(Vec_hConstraint)

class System(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, System, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, System, name)
    __repr__ = _swig_repr
    __swig_getmethods__["Failed"] = _slvs.System_Failed_get
    if _newclass:
        Failed = _swig_property(_slvs.System_Failed_get)
    __swig_setmethods__["GroupHandle"] = _slvs.System_GroupHandle_set
    __swig_getmethods__["GroupHandle"] = _slvs.System_GroupHandle_get
    if _newclass:
        GroupHandle = _swig_property(_slvs.System_GroupHandle_get, _slvs.System_GroupHandle_set)
    __swig_setmethods__["ParamHandle"] = _slvs.System_ParamHandle_set
    __swig_getmethods__["ParamHandle"] = _slvs.System_ParamHandle_get
    if _newclass:
        ParamHandle = _swig_property(_slvs.System_ParamHandle_get, _slvs.System_ParamHandle_set)
    __swig_setmethods__["EntityHandle"] = _slvs.System_EntityHandle_set
    __swig_getmethods__["EntityHandle"] = _slvs.System_EntityHandle_get
    if _newclass:
        EntityHandle = _swig_property(_slvs.System_EntityHandle_get, _slvs.System_EntityHandle_set)
    __swig_setmethods__["ConstraintHandle"] = _slvs.System_ConstraintHandle_set
    __swig_getmethods__["ConstraintHandle"] = _slvs.System_ConstraintHandle_get
    if _newclass:
        ConstraintHandle = _swig_property(_slvs.System_ConstraintHandle_get, _slvs.System_ConstraintHandle_set)
    __swig_getmethods__["Dof"] = _slvs.System_Dof_get
    if _newclass:
        Dof = _swig_property(_slvs.System_Dof_get)

    def __init__(self):
        this = _slvs.new_System()
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def reset(self):
        return _slvs.System_reset(self)

    def solve(self, group=0, reportFailed=False):
        return _slvs.System_solve(self, group, reportFailed)

    def getParam(self, h):
        return _slvs.System_getParam(self, h)

    def removeParam(self, h):
        return _slvs.System_removeParam(self, h)

    def addParam(self, v, overwrite=False):
        return _slvs.System_addParam(self, v, overwrite)

    def getConstraint(self, h):
        return _slvs.System_getConstraint(self, h)

    def removeConstraint(self, h):
        return _slvs.System_removeConstraint(self, h)

    def addConstraint(self, v, overwrite=False):
        return _slvs.System_addConstraint(self, v, overwrite)

    def getEntity(self, h):
        return _slvs.System_getEntity(self, h)

    def removeEntity(self, h):
        return _slvs.System_removeEntity(self, h)

    def addEntity(self, v, overwrite=False):
        return _slvs.System_addEntity(self, v, overwrite)

    def addParamV(self, val, group=0, h=0):
        return _slvs.System_addParamV(self, val, group, h)

    def addPoint2d(self, wrkpln, u, v, group=0, h=0):
        return _slvs.System_addPoint2d(self, wrkpln, u, v, group, h)

    def addPoint2dV(self, wrkpln, u, v, group=0, h=0):
        return _slvs.System_addPoint2dV(self, wrkpln, u, v, group, h)

    def addPoint3d(self, x, y, z, group=0, h=0):
        return _slvs.System_addPoint3d(self, x, y, z, group, h)

    def addPoint3dV(self, x, y, z, group=0, h=0):
        return _slvs.System_addPoint3dV(self, x, y, z, group, h)

    def addNormal3d(self, qw, qx, qy, qz, group=0, h=0):
        return _slvs.System_addNormal3d(self, qw, qx, qy, qz, group, h)

    def addNormal3dV(self, qw, qx, qy, qz, group=0, h=0):
        return _slvs.System_addNormal3dV(self, qw, qx, qy, qz, group, h)

    def addNormal2d(self, wrkpln, group=0, h=0):
        return _slvs.System_addNormal2d(self, wrkpln, group, h)

    def addDistance(self, d, group=0, h=0):
        return _slvs.System_addDistance(self, d, group, h)

    def addDistanceV(self, d, group=0, h=0):
        return _slvs.System_addDistanceV(self, d, group, h)

    def addLineSegment(self, p1, p2, group=0, h=0):
        return _slvs.System_addLineSegment(self, p1, p2, group, h)

    def addCubic(self, wrkpln, p1, p2, p3, p4, group=0, h=0):
        return _slvs.System_addCubic(self, wrkpln, p1, p2, p3, p4, group, h)

    def addArcOfCircle(self, wrkpln, center, start, end, group=0, h=0):
        return _slvs.System_addArcOfCircle(self, wrkpln, center, start, end, group, h)

    def addCircle(self, center, normal, radius, group=0, h=0):
        return _slvs.System_addCircle(self, center, normal, radius, group, h)

    def addCircleV(self, center, normal, radius, group=0, h=0):
        return _slvs.System_addCircleV(self, center, normal, radius, group, h)

    def addWorkplane(self, origin, normal, group=0, h=0):
        return _slvs.System_addWorkplane(self, origin, normal, group, h)

    def addTransform(self, src, dx, dy, dz, qw, qx, qy, qz, asAxisAngle=False, scale=1.0, timesApplied=0, group=0, h=0):
        return _slvs.System_addTransform(self, src, dx, dy, dz, qw, qx, qy, qz, asAxisAngle, scale, timesApplied, group, h)

    def addTranslate(self, src, dx, dy, dz, scale=1.0, timesApplied=0, group=0, h=0):
        return _slvs.System_addTranslate(self, src, dx, dy, dz, scale, timesApplied, group, h)

    def addConstraintV(self, tp, wrkpln, v, p1, p2, e1, e2, group=0, h=0):
        return _slvs.System_addConstraintV(self, tp, wrkpln, v, p1, p2, e1, e2, group, h)

    def addPointsDistance(self, d, p1, p2, wrkpln=0, group=0, h=0):
        return _slvs.System_addPointsDistance(self, d, p1, p2, wrkpln, group, h)

    def addPointsProjectDistance(self, d, p1, p2, line, group=0, h=0):
        return _slvs.System_addPointsProjectDistance(self, d, p1, p2, line, group, h)

    def addPointsCoincident(self, p1, p2, wrkpln=0, group=0, h=0):
        return _slvs.System_addPointsCoincident(self, p1, p2, wrkpln, group, h)

    def addPointPlaneDistance(self, d, pt, pln, group=0, h=0):
        return _slvs.System_addPointPlaneDistance(self, d, pt, pln, group, h)

    def addPointLineDistance(self, d, pt, line, wrkpln=0, group=0, h=0):
        return _slvs.System_addPointLineDistance(self, d, pt, line, wrkpln, group, h)

    def addPointInPlane(self, pt, pln, group=0, h=0):
        return _slvs.System_addPointInPlane(self, pt, pln, group, h)

    def addPointOnLine(self, pt, line, wrkpln=0, group=0, h=0):
        return _slvs.System_addPointOnLine(self, pt, line, wrkpln, group, h)

    def addEqualLength(self, l1, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addEqualLength(self, l1, l2, wrkpln, group, h)

    def addLengthRatio(self, ratio, l1, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addLengthRatio(self, ratio, l1, l2, wrkpln, group, h)

    def addLengthDifference(self, diff, l1, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addLengthDifference(self, diff, l1, l2, wrkpln, group, h)

    def addEqualLengthPointLineDistance(self, pt, l1, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addEqualLengthPointLineDistance(self, pt, l1, l2, wrkpln, group, h)

    def addEqualPointLineDistance(self, p1, l1, p2, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addEqualPointLineDistance(self, p1, l1, p2, l2, wrkpln, group, h)

    def addEqualAngle(self, supplement, l1, l2, l3, l4, wrkpln=0, group=0, h=0):
        return _slvs.System_addEqualAngle(self, supplement, l1, l2, l3, l4, wrkpln, group, h)

    def addEqualLineArcLength(self, line, arc, wrkpln=0, group=0, h=0):
        return _slvs.System_addEqualLineArcLength(self, line, arc, wrkpln, group, h)

    def addSymmetric(self, p1, p2, pln, wrkpln=0, group=0, h=0):
        return _slvs.System_addSymmetric(self, p1, p2, pln, wrkpln, group, h)

    def addSymmetricHorizontal(self, p1, p2, wrkpln, group=0, h=0):
        return _slvs.System_addSymmetricHorizontal(self, p1, p2, wrkpln, group, h)

    def addSymmetricVertical(self, p1, p2, wrkpln, group=0, h=0):
        return _slvs.System_addSymmetricVertical(self, p1, p2, wrkpln, group, h)

    def addSymmetricLine(self, p1, p2, line, wrkpln, group=0, h=0):
        return _slvs.System_addSymmetricLine(self, p1, p2, line, wrkpln, group, h)

    def addMidPoint(self, pt, line, wrkpln, group=0, h=0):
        return _slvs.System_addMidPoint(self, pt, line, wrkpln, group, h)

    def addPointsHorizontal(self, p1, p2, wrkpln, group=0, h=0):
        return _slvs.System_addPointsHorizontal(self, p1, p2, wrkpln, group, h)

    def addPointsVertical(self, p1, p2, wrkpln, group=0, h=0):
        return _slvs.System_addPointsVertical(self, p1, p2, wrkpln, group, h)

    def addLineHorizontal(self, line, wrkpln, group=0, h=0):
        return _slvs.System_addLineHorizontal(self, line, wrkpln, group, h)

    def addLineVertical(self, line, wrkpln, group=0, h=0):
        return _slvs.System_addLineVertical(self, line, wrkpln, group, h)

    def addDiameter(self, d, c, group=0, h=0):
        return _slvs.System_addDiameter(self, d, c, group, h)

    def addPointOnCircle(self, pt, circle, group=0, h=0):
        return _slvs.System_addPointOnCircle(self, pt, circle, group, h)

    def addSameOrientation(self, n1, n2, group=0, h=0):
        return _slvs.System_addSameOrientation(self, n1, n2, group, h)

    def addAngle(self, degree, supplement, l1, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addAngle(self, degree, supplement, l1, l2, wrkpln, group, h)

    def addPerpendicular(self, l1, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addPerpendicular(self, l1, l2, wrkpln, group, h)

    def addParallel(self, l1, l2, wrkpln=0, group=0, h=0):
        return _slvs.System_addParallel(self, l1, l2, wrkpln, group, h)

    def addArcLineTangent(self, atEnd, arc, line, group=0, h=0):
        return _slvs.System_addArcLineTangent(self, atEnd, arc, line, group, h)

    def addCubicLineTangent(self, atEnd, cubic, line, wrkpln=0, group=0, h=0):
        return _slvs.System_addCubicLineTangent(self, atEnd, cubic, line, wrkpln, group, h)

    def addCurvesTangent(self, atEnd1, atEnd2, c1, c2, wrkpln, group=0, h=0):
        return _slvs.System_addCurvesTangent(self, atEnd1, atEnd2, c1, c2, wrkpln, group, h)

    def addEqualRadius(self, c1, c2, group=0, h=0):
        return _slvs.System_addEqualRadius(self, c1, c2, group, h)

    def addWhereDragged(self, pt, wrkpln=0, group=0, h=0):
        return _slvs.System_addWhereDragged(self, pt, wrkpln, group, h)
    __swig_destroy__ = _slvs.delete_System
    __del__ = lambda self: None
System_swigregister = _slvs.System_swigregister
System_swigregister(System)

# This file is compatible with both classic and new-style classes.


