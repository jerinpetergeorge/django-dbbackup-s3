from unittest import TestCase, mock

from django.core.management import call_command


class S3BackupCommandTestCase(TestCase):
    @mock.patch("storage_sync.management.commands.s3backup.SyncS3Dropbox")
    def test_call_command(self, sync_mock):
        call_command("s3backup")
        sync_mock.assert_called_with(
            compress=False,
            dropbox_dir="upload-dir/",
            s3_bucket="",
            s3_dir="/",
            target_file_name="backup.tar.gz",
        )
