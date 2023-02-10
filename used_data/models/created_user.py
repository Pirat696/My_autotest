from typing import Any, Dict, List
from pydantic import BaseModel


class Category(BaseModel):
    id: str


class External(BaseModel):
    initiator: Any
    is_blocked: bool


class Self(BaseModel):
    is_blocked: bool


class BlockCall(BaseModel):
    external: External
    self: Self


class ListItem(BaseModel):
    id: str
    name: str
    roles: List[str]
    last_name: str
    first_name: str
    patronymic: str
    email: Any
    is_online: bool
    is_depend: bool
    is_active: bool
    is_company: bool
    is_client: bool
    language: Any
    parent: Any
    phone: str
    created_at: str
    bindings: List
    buildings: List
    signal_level: Any
    payload: Dict[str, Any]
    version: Any
    comment: Any
    source: str
    sources: Dict[str, Any]
    is_trusted: bool
    category: Category
    sip: Any
    block_call: BlockCall


class Metadata(BaseModel):
    total: int
    perPage: int
    pageCount: int
    page: int


class Model (BaseModel):
    list: List[ListItem]
    metadata: Metadata
    error: Any
