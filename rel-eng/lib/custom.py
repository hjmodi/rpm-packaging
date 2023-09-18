# Copyright (c) 2008-2014 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
import os

from tito.common import info_out, warn_out, error_out
from tito.compat import getstatusoutput
from tito.release import KojiReleaser, DistGitReleaser
from tito.release.distgit import extract_task_info

class BrewReleaser(KojiReleaser):

    def __init__(self, *args, **kwargs):
        if kwargs['releaser_config'].has_option(kwargs['target'], "offline"):
            kwargs['offline'] = True

        super(BrewReleaser, self).__init__(*args, **kwargs)

        self.executable = "brew"

    def _koji_release(self):
        if self.releaser_config.has_option(self.target, "scratch"):
            self.scratch = True

        super(BrewReleaser, self)._koji_release()

class SatelliteSixThreeReleaser(DistGitReleaser):

    def __init__(self, name=None, tag=None, build_dir=None,
            config=None, user_config=None,
            target=None, releaser_config=None, no_cleanup=False,
            test=False, auto_accept=False, **kwargs):
        print(target)

        DistGitReleaser.__init__(self, name, tag, build_dir, config,
                                 user_config, target, releaser_config, no_cleanup, test,
                                 auto_accept, **kwargs)
        if name.startswith('rubygem') or name.startswith('nodejs') or name.startswith('python'):
            remote_git_name = name
            if target == 'scl-ror52-dist-git-rhel-7':
                remote_git_name = 'tfm-ror52-' + remote_git_name
            elif target == 'scl-dist-git-rhel-7':
                remote_git_name = 'tfm-' + remote_git_name
            elif target == 'dist-git-rhel-7' and name.startswith('python'):
                remote_git_name = 'tfm-pulpcore-' + remote_git_name

            # Taken out of FedoraGitReleaser, these values need to be reset
            self.project_name = remote_git_name

            self.package_workdir = os.path.join(self.working_dir,
                                                self.project_name)

    def _build(self, branch):
        """ Submit a rhpkg build from current directory. """
        target_param = ""
        scratch_param = ""
        build_target = self._get_build_target_for_branch(branch)
        if build_target:
            target_param = "--target %s" % build_target
        if self.scratch:
            scratch_param = "--scratch"

        build_cmd = "%s build --nowait --skip-nvr-check %s %s" % (self.cli_tool, scratch_param, target_param)

        if self.dry_run:
            self.print_dry_run_warning(build_cmd)
            return

        info_out("Submitting build: %s" % build_cmd)
        (status, output) = getstatusoutput(build_cmd)
        if status > 0:
            if "already been built" in output:
                warn_out("Build has been submitted previously, continuing...")
            else:
                error_out([
                    "Unable to submit build."
                    "  Status code: %s\n" % status,
                    "  Output: %s\n" % output,
                ])

        # Print the task ID and URL:
        for line in extract_task_info(output):
            print(line)
