"""Pydantic schemas"""
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date


class Performance(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    performance_id: int
    player_id: int
    week_number: str
    fantasy_points: float
    last_changed_date: date


class PlayerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    player_id: int
    gsis_id: str
    first_name: str
    last_name: str
    position: str
    last_changed_date: date


class Player(PlayerBase):
    model_config = ConfigDict(from_attributes=True)
    performances: List[Performance] = []
