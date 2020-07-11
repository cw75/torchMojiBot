# coding: utf-8

"""
    Algorithmia Management APIs

    APIs for managing actions on the Algorithmia platform  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: support@algorithmia.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class VersionInfoPublish(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'version_type': 'VersionType',
        'release_notes': 'str',
        'sample_input': 'str',
        'sample_output': 'str'
    }

    attribute_map = {
        'version_type': 'version_type',
        'release_notes': 'release_notes',
        'sample_input': 'sample_input',
        'sample_output': 'sample_output'
    }

    def __init__(self, version_type=None, release_notes=None, sample_input=None, sample_output=None):  # noqa: E501
        """VersionInfoPublish - a model defined in OpenAPI"""  # noqa: E501

        self._version_type = None
        self._release_notes = None
        self._sample_input = None
        self._sample_output = None
        self.discriminator = None

        if version_type is not None:
            self.version_type = version_type
        if release_notes is not None:
            self.release_notes = release_notes
        if sample_input is not None:
            self.sample_input = sample_input
        if sample_output is not None:
            self.sample_output = sample_output

    @property
    def version_type(self):
        """Gets the version_type of this VersionInfoPublish.  # noqa: E501


        :return: The version_type of this VersionInfoPublish.  # noqa: E501
        :rtype: VersionType
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this VersionInfoPublish.


        :param version_type: The version_type of this VersionInfoPublish.  # noqa: E501
        :type: VersionType
        """

        self._version_type = version_type

    @property
    def release_notes(self):
        """Gets the release_notes of this VersionInfoPublish.  # noqa: E501


        :return: The release_notes of this VersionInfoPublish.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this VersionInfoPublish.


        :param release_notes: The release_notes of this VersionInfoPublish.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

    @property
    def sample_input(self):
        """Gets the sample_input of this VersionInfoPublish.  # noqa: E501


        :return: The sample_input of this VersionInfoPublish.  # noqa: E501
        :rtype: str
        """
        return self._sample_input

    @sample_input.setter
    def sample_input(self, sample_input):
        """Sets the sample_input of this VersionInfoPublish.


        :param sample_input: The sample_input of this VersionInfoPublish.  # noqa: E501
        :type: str
        """

        self._sample_input = sample_input

    @property
    def sample_output(self):
        """Gets the sample_output of this VersionInfoPublish.  # noqa: E501


        :return: The sample_output of this VersionInfoPublish.  # noqa: E501
        :rtype: str
        """
        return self._sample_output

    @sample_output.setter
    def sample_output(self, sample_output):
        """Sets the sample_output of this VersionInfoPublish.


        :param sample_output: The sample_output of this VersionInfoPublish.  # noqa: E501
        :type: str
        """

        self._sample_output = sample_output

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VersionInfoPublish):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other