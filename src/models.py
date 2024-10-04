from pydantic import BaseModel
from enum import Enum


class PredictionType(str, Enum):
    classification = "CLS"
    object_detection = "OD"
    segmentation = "SEG"


class GunType(str, Enum):
    pistol = "pistol"
    rifle = "rifle"


class PersonType(str, Enum):
    safe = "safe"
    danger = "danger"


class PixelLocation(BaseModel):
    x: int
    y: int


class GeneralPrediction(BaseModel):
    pred_type: PredictionType


class Detection(GeneralPrediction):
    n_detections: int
    boxes: list[list[int]]
    labels: list[str]
    confidences: list[float]


class Segmentation(GeneralPrediction):
    n_detections: int
    polygons: list[list[list[int]]]
    boxes: list[list[int]]
    labels: list[str]


class Gun(BaseModel):
    gun_type: GunType
    location: PixelLocation

class Person(BaseModel):
    person_type: PersonType
    location: PixelLocation
    area: int