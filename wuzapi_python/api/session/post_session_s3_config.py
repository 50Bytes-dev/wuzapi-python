from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_session_s3_config_response_200 import PostSessionS3ConfigResponse200
from ...models.s3_config import S3Config
from ...types import Response


def _get_kwargs(
    *,
    body: S3Config,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/s3/config",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostSessionS3ConfigResponse200]]:
    if response.status_code == 200:
        response_200 = PostSessionS3ConfigResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PostSessionS3ConfigResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: S3Config,
) -> Response[Union[Any, PostSessionS3ConfigResponse200]]:
    """Configure S3 Storage

     Configures S3 storage settings for the user to store media files.
    Supports AWS S3, MinIO, Backblaze B2, and other S3-compatible services.
    When enabled, media files will be uploaded to S3 and can be accessed via public URLs.

    Args:
        body (S3Config):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostSessionS3ConfigResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: S3Config,
) -> Optional[Union[Any, PostSessionS3ConfigResponse200]]:
    """Configure S3 Storage

     Configures S3 storage settings for the user to store media files.
    Supports AWS S3, MinIO, Backblaze B2, and other S3-compatible services.
    When enabled, media files will be uploaded to S3 and can be accessed via public URLs.

    Args:
        body (S3Config):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostSessionS3ConfigResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: S3Config,
) -> Response[Union[Any, PostSessionS3ConfigResponse200]]:
    """Configure S3 Storage

     Configures S3 storage settings for the user to store media files.
    Supports AWS S3, MinIO, Backblaze B2, and other S3-compatible services.
    When enabled, media files will be uploaded to S3 and can be accessed via public URLs.

    Args:
        body (S3Config):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostSessionS3ConfigResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: S3Config,
) -> Optional[Union[Any, PostSessionS3ConfigResponse200]]:
    """Configure S3 Storage

     Configures S3 storage settings for the user to store media files.
    Supports AWS S3, MinIO, Backblaze B2, and other S3-compatible services.
    When enabled, media files will be uploaded to S3 and can be accessed via public URLs.

    Args:
        body (S3Config):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostSessionS3ConfigResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
