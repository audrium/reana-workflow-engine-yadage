# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
"""REANA-Workflow-Engine-yadage utility functions."""

from reana_commons.publisher import WorkflowStatusPublisher


class REANAWorkflowStatusPublisher(object):
    """REANA workflow status publisher singleton."""

    __instance = None

    def __new__(cls, instance=None):
        """REANA workflow status publisher object creation."""
        if instance:
            REANAWorkflowStatusPublisher.__instance = instance
        elif REANAWorkflowStatusPublisher.__instance is None:
            REANAWorkflowStatusPublisher.__instance = WorkflowStatusPublisher()
        return REANAWorkflowStatusPublisher.__instance
