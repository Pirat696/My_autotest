from typing import Any, Dict, List
from pydantic import BaseModel

class AppVersion(BaseModel):
    versionCode: Any
    versionName: Any


class Payload(BaseModel):
    appVersion: AppVersion
    systemVersion: Any
    deviceType: Any
    model: Any
    manufacturer: Any
    brand: Any
    platform: Any
    BundleId: Any


class Category(BaseModel):
    id: str
    alias: str
    title: str


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
    last_name: Any
    first_name: Any
    patronymic: Any
    email: str
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
    auth: List
    buildings: List
    signal_level: Any
    payload: Payload
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
    can_edit: bool
    can_delete: bool
    roles: List[str]
    latest_version: Dict[str, Any]


class Model(BaseModel):
    list: List[ListItem]
    metadata: Metadata
    error: Any