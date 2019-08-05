# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2019 Aspose.PDF Cloud
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.



    OpenAPI spec version: 3.0
    
"""


from pprint import pformat
from six import iteritems
import re


class Attachment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'list[Link]',
        'description': 'str',
        'mime_type': 'str',
        'name': 'str',
        'creation_date': 'str',
        'modification_date': 'str',
        'size': 'int',
        'check_sum': 'str'
    }

    attribute_map = {
        'links': 'Links',
        'description': 'Description',
        'mime_type': 'MimeType',
        'name': 'Name',
        'creation_date': 'CreationDate',
        'modification_date': 'ModificationDate',
        'size': 'Size',
        'check_sum': 'CheckSum'
    }

    def __init__(self, links=None, description=None, mime_type=None, name=None, creation_date=None, modification_date=None, size=None, check_sum=None):
        """
        Attachment - a model defined in Swagger
        """

        self._links = None
        self._description = None
        self._mime_type = None
        self._name = None
        self._creation_date = None
        self._modification_date = None
        self._size = None
        self._check_sum = None

        if links is not None:
          self.links = links
        if description is not None:
          self.description = description
        if mime_type is not None:
          self.mime_type = mime_type
        if name is not None:
          self.name = name
        if creation_date is not None:
          self.creation_date = creation_date
        if modification_date is not None:
          self.modification_date = modification_date
        self.size = size
        if check_sum is not None:
          self.check_sum = check_sum

    @property
    def links(self):
        """
        Gets the links of this Attachment.
        Link to the document.

        :return: The links of this Attachment.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Attachment.
        Link to the document.

        :param links: The links of this Attachment.
        :type: list[Link]
        """

        self._links = links

    @property
    def description(self):
        """
        Gets the description of this Attachment.
        Gets text associated with the attachment. 

        :return: The description of this Attachment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Attachment.
        Gets text associated with the attachment. 

        :param description: The description of this Attachment.
        :type: str
        """

        self._description = description

    @property
    def mime_type(self):
        """
        Gets the mime_type of this Attachment.
        Gets subtype of the attachment file.

        :return: The mime_type of this Attachment.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this Attachment.
        Gets subtype of the attachment file.

        :param mime_type: The mime_type of this Attachment.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def name(self):
        """
        Gets the name of this Attachment.
        Gets the name of the attachment. 

        :return: The name of this Attachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Attachment.
        Gets the name of the attachment. 

        :param name: The name of this Attachment.
        :type: str
        """

        self._name = name

    @property
    def creation_date(self):
        """
        Gets the creation_date of this Attachment.
        The date and time when the embedded file was created.

        :return: The creation_date of this Attachment.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this Attachment.
        The date and time when the embedded file was created.

        :param creation_date: The creation_date of this Attachment.
        :type: str
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """
        Gets the modification_date of this Attachment.
        The date and time when the embedded file was last modified.

        :return: The modification_date of this Attachment.
        :rtype: str
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """
        Sets the modification_date of this Attachment.
        The date and time when the embedded file was last modified.

        :param modification_date: The modification_date of this Attachment.
        :type: str
        """

        self._modification_date = modification_date

    @property
    def size(self):
        """
        Gets the size of this Attachment.
        The size of the uncompressed embedded file, in bytes.

        :return: The size of this Attachment.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Attachment.
        The size of the uncompressed embedded file, in bytes.

        :param size: The size of this Attachment.
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size

    @property
    def check_sum(self):
        """
        Gets the check_sum of this Attachment.
        A 16-byte string that is the checksum of the bytes of the uncompressed embedded file.  The checksum is calculated by applying the standard MD5 message-digest algorithm  to the bytes of the embedded file stream.

        :return: The check_sum of this Attachment.
        :rtype: str
        """
        return self._check_sum

    @check_sum.setter
    def check_sum(self, check_sum):
        """
        Sets the check_sum of this Attachment.
        A 16-byte string that is the checksum of the bytes of the uncompressed embedded file.  The checksum is calculated by applying the standard MD5 message-digest algorithm  to the bytes of the embedded file stream.

        :param check_sum: The check_sum of this Attachment.
        :type: str
        """

        self._check_sum = check_sum

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Attachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
