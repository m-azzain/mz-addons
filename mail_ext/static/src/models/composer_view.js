/** @odoo-module **/
/*Do not forget to add the first above comment to your javascript files files*/

/*Every thing here has been copied from the original file mail/static/src/models/composer_view.js*/
/*You are free to add anything to the context*/
/*like
'from_full_composer': true
this is the only addition to the original content

If you want to override a method but still want to call it from your new overriding method, you can use this._super(passed_arguments)
*/

/*These imports, you can delete whatever that you don't want*/
import { registerModel } from '@mail/model/model_core';
import { attr, many, one } from '@mail/model/model_field';
import { clear, insertAndReplace, link, replace, unlink } from '@mail/model/model_field_command';
import { OnChange } from '@mail/model/model_onchange';
import { addLink, escapeAndCompactTextContent, parseAndTransform } from '@mail/js/utils';
import { isEventHandled, markEventHandled } from '@mail/utils/utils';

import { escape, sprintf } from '@web/core/utils/strings';
import { url } from '@web/core/utils/urls';

import { patchRecordMethods } from '@mail/model/model_core';
patchRecordMethods(
    'ComposerView', {
        /**
         * Open the full composer modal.
         */
        async openFullComposer() {
            const attachmentIds = this.composer.attachments.map(attachment => attachment.id);
            const context = {
                default_attachment_ids: attachmentIds,
                default_body: escapeAndCompactTextContent(this.composer.textInputContent),
                default_is_log: this.composer.isLog,
                default_model: this.composer.activeThread.model,
                default_partner_ids: this.composer.recipients.map(partner => partner.id),
                default_res_id: this.composer.activeThread.id,
                mail_post_autofollow: this.composer.activeThread.hasWriteAccess,

                from_full_composer: true,
            };

            const action = {
                type: 'ir.actions.act_window',
                res_model: 'mail.compose.message',
                view_mode: 'form',
                views: [[false, 'form']],
                target: 'new',
                context: context,
            };
            const composer = this.composer;
            const options = {
                onClose: () => {
                    if (!composer.exists()) {
                        return;
                    }
                    composer._reset();
                    if (composer.activeThread) {
                        composer.activeThread.fetchData(['messages']);
                    }
                },
            };
            await this.env.services.action.doAction(action, options);
        }
    }
);