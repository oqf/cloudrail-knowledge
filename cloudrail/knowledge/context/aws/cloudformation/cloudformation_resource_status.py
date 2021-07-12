from enum import Enum


class CloudformationResourceStatus(Enum):

    CREATE_IN_PROGRESS = 'CREATE_IN_PROGRESS'
    CREATE_FAILED = 'CREATE_FAILED'
    CREATE_COMPLETE = 'CREATE_COMPLETE'
    ROLLBACK_IN_PROGRESS = 'ROLLBACK_IN_PROGRESS'
    ROLLBACK_FAILED = 'ROLLBACK_FAILED'
    ROLLBACK_COMPLETE = 'ROLLBACK_COMPLETE'
    DELETE_IN_PROGRESS = 'DELETE_IN_PROGRESS'
    DELETE_FAILED = 'DELETE_FAILED'
    DELETE_COMPLETE = 'DELETE_COMPLETE'
    UPDATE_IN_PROGRESS = 'UPDATE_IN_PROGRESS'
    UPDATE_COMPLETE_CLEANUP_IN_PROGRESS = 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'
    UPDATE_COMPLETE = 'UPDATE_COMPLETE'
    UPDATE_ROLLBACK_IN_PROGRESS = 'UPDATE_ROLLBACK_IN_PROGRESS'
    UPDATE_ROLLBACK_FAILED = 'UPDATE_ROLLBACK_FAILED'
    UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS = 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'
    UPDATE_ROLLBACK_COMPLETE = 'UPDATE_ROLLBACK_COMPLETE'
    REVIEW_IN_PROGRESS = 'REVIEW_IN_PROGRESS'
    IMPORT_IN_PROGRESS = 'IMPORT_IN_PROGRESS'
    IMPORT_COMPLETE = 'IMPORT_COMPLETE'
    IMPORT_ROLLBACK_IN_PROGRESS = 'IMPORT_ROLLBACK_IN_PROGRESS'
    IMPORT_ROLLBACK_FAILED = 'IMPORT_ROLLBACK_FAILED'
    IMPORT_ROLLBACK_COMPLETE = 'IMPORT_ROLLBACK_COMPLETE'
